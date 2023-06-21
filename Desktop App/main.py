from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
import serial


def main():
    # setup
    # read serial data from a correct port, and correct baud rate
    ser = serial.Serial('COM4', baudrate=115200, timeout=0.05)
    print("Device connected")

    # main loop
    while True:
        # try so it doesn't stop on occasional errors
        try:
            serial_input = str(ser.readline())
            # a bit print and escape sequence are being read, so we have to strip them
            x = serial_input[2:-5]

            # serial data is a one string, so we have to separate it and make into integers
            volume_levels = x.split(" ")
            volume_levels_ints = list(map(int, volume_levels))
            # print(volume_levels_ints)

            # change main volume
            change_main_volume(volume_levels_ints[0])

            # change volume of an app
            # we can assign multiple apps to the same potentiometer
            # note: some processes are capitalised and some are not, check their names in the task manager

            # voice chats
            change_app_volume(volume_levels_ints[1], "Discord")

            # music
            change_app_volume(volume_levels_ints[2], "Spotify")

            # browsers
            change_app_volume(volume_levels_ints[3], "firefox")

            # games
            change_app_volume(volume_levels_ints[4], "stellaris")
            change_app_volume(volume_levels_ints[4], "eldenring")

        except ValueError:
            print("ValueError (Probably no new data to receive)")


# input = volume level
def change_main_volume(input_volume):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(input_volume / 100, None)


# input1 = volume level, input2= app name (without .exe)
def change_app_volume(input_volume, input_application):
    count = False
    app = input_application + ".exe"
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == app:
            count = True
            volume.SetMasterVolume(input_volume / 100, None)
    if not count:
        print("App " + input_application + " not found")


if __name__ == "__main__":
    main()

# TODO
