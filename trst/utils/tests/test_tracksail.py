from trst.utils.tracksail_utils import TrackSailInterface

def test_tracksail_interface():
    interface = TrackSailInterface()
    print(interface.wind_direction)

if __name__ == '__main__':
    test_tracksail_interface()
