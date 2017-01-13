import rx

class DataTransformer(rx.Observer, rx.Observable):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._observable = rx.subjects.Subject()

    def subscribe(self, on_next=None, on_error=None,
                  on_completed=None, observer=None):
        self._observable.subscribe(on_next=on_next, on_error=on_error,
                                   on_completed=on_completed,
                                   observer=observer)

    def on_next(self, value):
        self.process_data(value)

    def on_completed(self):
        self.process_complete()
        self._observable.on_completed()

    def on_error(self, error):
        self._observable.on_error(error)

    def emit_result(self, value):
        self._observable.on_next(output_value)

    @abstractmethod
    def process_data(self, value):
        """
        Abstract method for processing the datum. Emit to observers
        by calling emit_result
        """
        pass

    @abstractmethod
    def process_complete(self):
        """
        Abstract method for data processing completion. Called before on
        complete is called
        """
        pass
