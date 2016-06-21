import os
import numpy as np
import tensorflow as tf


class Detector:
    def __init__(self, file_path):
        self.file_path = file_path
        pwd = os.path.dirname(os.path.realpath(__file__))
        self.modelFullPath = pwd + '/graph/output_graph.pb'
        self.labelsFullPath = pwd +  '/graph/output_labels.txt'

    def run(self):
        self._load_graph()
        return self._detect()

    def _load_graph(self):
        with tf.gfile.FastGFile(self.modelFullPath, 'rb') as f:
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(f.read())
                _ = tf.import_graph_def(graph_def, name='')

    def _detect(self):
        image_data = tf.gfile.FastGFile(self.file_path, 'rb').read()
        with tf.Session() as sess:
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            predictions = sess.run(softmax_tensor,
                                   {'DecodeJpeg/contents:0':image_data})
            predictions = np.squeeze(predictions)
            top_k = predictions.argsort()[-5:][::-1]  # Getting top 5 predictions
        top_k = predictions.argsort()[-5:][::-1]  # Getting top 5 predictions
        f = open(self.labelsFullPath, 'rb')
        lines = f.readlines()
        labels = [w.decode("utf-8").replace("\n", "") for w in lines]
        answers = dict()
        i = 0
        for node_id in top_k:
            answer = dict(label=labels[node_id], score=str(predictions[node_id]))
            answers[str(i)] = answer
            i= i + 1
        return answers
