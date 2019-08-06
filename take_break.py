"""
set an alarm to take a break by playing a youtube video
Wayne's follow-up: This worked great.  60 minutes after launching the program,
 a youtube video automatically lunched.
"""
import webbrowser
import time


def main ():
    """'Test function
    :return: none
    """
    video_address = "https://www.youtube.com/watch?v=GWzNciObAHY"
    # delay "sleep"
    counter = 0
    while counter < 3:
        time.sleep(60*60)    # delay the start for 3 seconds ; 1 hr
        webbrowser.open(video_address)
        counter += 1
        print ("It is time to take a break, is: ", time.ctime())

if __name__ == '__main__':
    main()
    exit(0)

