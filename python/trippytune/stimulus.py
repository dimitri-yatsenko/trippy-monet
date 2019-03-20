

class StimulusMovie:
    """
    Abstract stimulus movie
    """

    def get_intensity_frame(self, frame):
        """
        :param frame: number (can be fractional)
        :return: intensity frame corresponding to time
        """


class Session:

    def __init__(self, traces, times):
        """
        :param traces: array of size (T, N) array where T = number of time samples, N = number of units
        :param times: array of size (T,) with sample times of the traces
        """
        self.traces = traces
        self.times = times
        self.trials = []  # list of pairs (StimulusMovie, timestamps)

    def add_trial(self, stimulus_movie: StimulusMovie, frame_times):
        """
        :param stimulus_movie: an object of type StimulusMovie
        :param frame_times: (s) array of size (T,)
        """
        if stimulus_movie.nframes != frame_times.size:
            raise IndexError('frame times must match stimulus movie')
        self.trials.append((stimulus_movie, frame_times))

    def compute_receptive_fields(self, taps, nx=None, ny=None):
        """
        :param taps: scalar or 1D array of size (M,) containing the delays from stimulus to measurement
        :param nx:
        :param ny:
        :return: array of size (N, Y, X) if taps is scalar or (N, Y, X, M) if taps is a (M,) vector
        """
        raise NotImplementedError
