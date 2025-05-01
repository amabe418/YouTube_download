

import yt_dlp as dlp

def download_video(link):
    opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4'
    }

    try:
        with dlp.YoutubeDL(opts) as dl:
            dl.download([link])
        print("ya se hizo esta vaina")

    except Exception as e:
        print("no se pudo")    

links = [
    # "https://youtu.be/rOeFK8IVa0c?si=l1P-AAoxikpkIeY0",
    # "https://youtu.be/sOE6hRa0Fus?si=V2nHlgzT-NO-HoZW",
    # "https://youtu.be/GXwsLwediL0?si=ScqaLqRuncAdl8if",
    # "https://youtu.be/lZlQmGG1KsU?si=UkgwXeGvLOMNkzRA",
    # "https://youtu.be/H4MfvgqsYPQ?si=Yf9zelnhN5BjJUWd",
    # "https://youtu.be/rjSxbMaDPl4?si=e2Ut1seq8oSZzy1r",
    # "https://youtu.be/JT6S5HW3-WU?si=QTDpBTeDHHVyFFZy",
    # "https://youtu.be/PyMwNMxTyFU?si=1RrNIFwoSYDwRTWp",
    # "https://youtu.be/xNV9hZcX25k?si=aW0z0Vf9fEBME3gu",
    # "https://youtu.be/Kcb_iV1EJZs?si=zJkS1N4WQ8bJ5Vsk",
    # "https://youtu.be/OGO0qPrFpNw?si=T2NFQEnHDk6j_eCQ",
    "https://youtu.be/vRpLar4IbUI?si=xjsrTCL219M-tgk0",
    "https://youtu.be/VmNfT22Dd3s?si=Mey-KNRuVS92bAk9",
    "https://youtu.be/p484eCNmuwM?si=2ljwffLdGUZCTj80",
    "https://youtu.be/W-TnLwP9sHw?si=Y2X3r9cIm7FW2vbc",
    "https://youtu.be/_3qEnzZHt70?si=k5orBKwbQjxCcNpV",
    "https://youtu.be/2JMhULiWvXw?si=fnKrrb2K00ZEPkPK",
    "https://youtu.be/aZhjdrbapgA?si=sZ4ihoj_a1y0YitV",
    "https://youtu.be/IqrCisB5384?si=W3tnCTNDsMYldPcv",
    "https://youtu.be/dptT47Y7QZI?si=0BI8jf8U55AHzFTk",
    "https://youtu.be/Kpu3bkA9kHY?si=FqyLfImW0R2Anbim",
    "https://youtu.be/2UqqC2u533c?si=hMrBIgBkN5V2DKGd",
    "https://youtu.be/Focd3AAttVs?si=pyO0X8JV92GIJAH3",
    "https://youtu.be/-o_Co3MYe9I?si=TNwkvr73iQvML-Su"
] 

for link in links:
    download_video(link)





 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 
