import Leap
import sys


class SampleListener(Leap.Listener):
    def on_init(self, controller):
        print("Initialized")

    def on_connect(self, controller):
        print("Connected")

    def on_disconnect(self, controller):
        print("Disconnected")

    def on_exit(self, controller):
        print("Exited")

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        hands = frame.hands
        numHands = len(hands)
        print("Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d" % (
            frame.id, frame.timestamp, numHands, len(frame.fingers), len(frame.tools)))

        if numHands >= 1:
            # Get the first hand
            hand = hands[0]

            # Check if the hand has any fingers
            fingers = hand.fingers
            numFingers = len(fingers)
            if numFingers >= 1:
                # Calculate the hand's average finger tip position
                pos = Leap.Vector()
                for finger in fingers:
                    pos += finger.tip_position

                pos = pos.__div__(numFingers)
                print("Hand has", numFingers,
                      "fingers with average tip position", pos)

            # Get the palm position
            palm = hand.palm_position
            print("Palm position:", palm)

            # Get the palm normal vector  and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            print("Pitch: %f degrees,  Roll: %f degrees,  Yaw: %f degrees" % (
                direction.pitch * Leap.RAD_TO_DEG,
                normal.roll * Leap.RAD_TO_DEG,
                direction.yaw * Leap.RAD_TO_DEG))

            print("Hand curvature radius: %f mm" % hand.sphere_radius)


def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print("Press Enter to quit...")
    sys.stdin.readline()

    # Remove the sample listener when done
    controller.remove_listener(listener)


if __name__ == "__main__":
    main()
