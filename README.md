## Latte Viewer
Latte Viewer is a program to convert latte files to png files or image files to latte files.  
It supports JPG, JPEG and PNG files.  
You can convert latte files to only png format.  
**NOTE:** I'm NOT recommending using translucent files! Latte doesn't supports alpha value, your program can be CRASHED!

An Image file to Latte format  
![GUI_IMG1](https://lh3.googleusercontent.com/RoDGd50htLfTVavXAtEQ-QeAPQdr80onrcFNGS1Fd3r2PJFEk9Qh3h9axXnaDiiiBOs4BdotzHelkf2-ouMX2LvuQuyjLq7RxhgnANY7JBPDXDVPNq4vz2EdNY51VjYzXNSEaztiwOpi2y61cC-D_xwFCCgwrlhfBBkgdNod586U_Ux-TSlSizcT2XUthTZfGUUXnHlYqyqigbcsXoWbbIBd2ubAi8RqsYbUKlo-hDpY4lMo_zH1whnFMU-F4pJJulSkSkfWUDVjc09-R5ijC2lMdhXZDTvsfQQPRcAcgyJW8DvFyPeZqwclDiHJI-uT42Nl-lv92UD4QCol3Ams1eyk0bPgmWH6b5pClZbgUSRooe2ysF2YB85SLHyAWHHKvGUwPMyZqRy0p7pzcNQ6TBht_kHQSa7nD1zO4BtCcnC8fiZOrgFWrQzeEypyfQIf5MQ9A_gHr6nTv49JOjRSo6PyOJ3QguveBR38XNIC_va-X99K11TbCKIEtmn57iilbnazuSC3bMswjVe9ddhpSFiLof8BWAtD6WqkZ-qXkhNoKPNk-BCJDVxTGhkW7HCFxLacbkGUVHE1t347tM6tqez3wYIt8zsBLlgS54-wIV0eGKiPzDTplkjAyEesvZ9Wf_sj1yqCq-O9K63RTfJQerXCx3CwpldPqX48F3n__3qmnawz_RTGlnVDFc5zhw=w800-h524-no?authuser=0)  
  
A Latte file to Image format  
![GUI_IMG2](https://lh3.googleusercontent.com/dgeAWfAdkWUvQr0HQ9cp7P7Fh63SvkEhQTXfFw0ENO6bw5n58PYtUS-km81rSW2sNkIlajmUNi7l3Bp6C-o4PC-lXMbhtWco5zDaizCIrZhRT65KaNrPXMeCIHVpPuibs3mLQYQKvJe9Cytcx93bHGGpktEDE6VO19eu7QJVZxkXeKT2KjR4gLEFginPYFSx81-7ZRAVqoxgstbRouNGk8j1RraRbht3vnVgdSOpOqd8Eosf_IciHXcnphpocsQ7CnfrJ4xvnhpqd8Wa_c_jHT-X-noNUIKs_N9RFxBMBpwnVlzXOzt_zMY-7O9D87VCmrFE2iKDkRurzHi6j5jNqrTSyyRVlmPyXdxeWLkZcJ8YKPrdv9Qg-cCDq8GsCb2sihvYpeN15RMyXjSs-0bZp2bUd8klZA8MWfoKewi1fRJaCc9hi9jQ9YI50rN5fjgvhKPQEG3QN30fjdKajs0GBL3JnAZNiP5RVDHXJqITltnStc3KiTb9R1JAuiPrf9feGauYsZWRLGQSakGui0mpbV9Q_4JcVCB0HnjmTmCEYCF-fewK2fiE4FeIHV4ES8g8VkSlI34bzewnr5aWh2tAtjQCCCglnpzghIzZZjrsq2DHmB6AyxSlwn05Xa-nfhCYJrLheGTdzmHoWLoSZbhhx0PTvtEuxGAR5GsfYUIxLws4TH2yr1b7CQuPo67RtA=w800-h524-no?authuser=0)  
  
The listbox at top-left shows the .latte, .jpg, .jpeg and .png files in the same folder.  
The entry at top-right of listbox for browsing the file with path.  
The button at the right of the entry for browse the path.  
The button at middle-right of GUI for saving the file as .png or .latte file.  

## Latte Files
Latte files not work like other image files, they work like lists.  
Example, you have two png files, and they have same image. But their size are different. Because PNG files uses a compression to make the size smaller.  
Latte files are programmer-friendly, because they works like lists and that makes it easier to edit it.  
There is modules to edit image files, but it can be faster to create new image files.  
Latte files work like that:  
\<width\>,\<pixel1red\>\<pixel1green\>\<pixel1blue\>\<pixel2red\>\<pixel2green\>\<pixel2blue\>...  
Example:  
3,!!!z!!zz!zzz!zz!!z!z!z!zzzz  
3 is width of image.  
!'s Decimal Value is 33.  
z's Decimal Value is 122.  
  
<pre>
Pixel 1: !!!   RGB: 33,33,33         Color: Darker than Gray  
Pixel 2: z!!   RGB: 122,33,33        Color: Darker and Paler than Red  
Pixel 3: zz!   RGB: 122,122,33       Color: Darker and Paler than Yellow  
Pixel 4: zzz   RGB: 122,122,122      Color: Gray  
Pixel 5: !zz   RGB: 33,122,122       Color: Darker and Paler than Cyan  
Pixel 6: !!z   RGB: 33,33,122        Color: Darker and Paler than Blue  
Pixel 7: !z!   RGB: 33,122,33        Color: Darker and Paler than Green  
Pixel 8: z!z   RGB: 122,33,122       Color: Darker and Paler than Magenta  
Pixel 9: zzz   RGB: 122,122,122      Color: Gray 
</pre>

![Example Image](https://lh3.googleusercontent.com/os7PrswZHl96cVFTyQTrqBaGt_Xyh6EyWuju8gWXtOP_RJiCOvwOc81h8GKvkuBIcGeuUaBe-xcQFddweLQmXPi-OIY3WSb2nUUvt0wXGWHNPE6gH9W2mAe9wKQZenaKaO6LJ5EZ2_il4DM1yJ1TvC5grRLX0zBtzoE3XxyqYx7uFneFBqVO7yqa_p7hRmB1LqqVaekQg9uIlAt3K8T2yiS2SMwdePybe8MPRsptgm718rLR8e7oekkV6YSvPbokCYipw7RhMLA6DMRidDRhjv-4wJSUIwwUy18DZKpA4qUadsA8ZAk5rS19blTLHs1JMlHVRm4KfqIeLjfnlk49rRegJmKv_zh0xeWM87zFzI2B27GLHQK5a9QH1p1CtOW8QhHaU1YEi-RI6KukBtRgAScvpr1sHxmQt9Jq4Y4xMv9kpqvVhe15jLlv9cOu5406z4WEz-h54a-Z5JOdKQijesaNoBQkrLM5g_7nwWYYZYUB2Fu4SuydcEI2EyV1BKC2SZhdapzQh1gBxAlwKc4UNUekKzyY2czemoGMdLnZ0NfbFdYvPyFUtbvCz2W9Da6kjTmLRbjoKicbfaabwWseI5tsK8mvd5zW1chRzCskIpWpQ25jWaPkNEv-yoMS_cft31nrgjXpyg63m1onMZiQwqpr-JGXEwqwQWQ6UTAlKe-1TDRymnqwneaRmo7chQ=w500-h400-no?authuser=0)
