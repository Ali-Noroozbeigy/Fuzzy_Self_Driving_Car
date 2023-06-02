class FuzzyGasController:
    """
    # emtiazi todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        self.inference_results = None
        

    def decide(self, center_dist):
        """
        main method for doin all the phases and returning the final answer for gas
        """
        return 30

    def membership_degree_front(self, front_distance):
        return {
            'close': self.close(front_distance),
            'moderate': self.moderate(front_distance),
            'far': self.far(front_distance)
        }

    def close(self, x):
        if 0 <= x <= 50:
            return (-1/50) * x + 1
        return 0

    def moderate(self, x):
        if 40 <= x <= 50:
            return (1/10) * x - 4
        if 50 < x <= 100:
            return (-1/50) * x + 2
        return 0

    def far(self, x):
        if 90 <= x <= 200:
            return (1/110) * x - (9/11)

    def inference(self, f_memship):
        self.inference_results = {
            'low': f_memship['close'],
            'medium': f_memship['moderate'],
            'high': f_memship['far']
        }
