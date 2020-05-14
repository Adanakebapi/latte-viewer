## Latte Viewer
Latte Viewer is a program to convert latte files to png files or image files to latte files.  
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
  
Pixel 1: !!!   RGB: 33,33,33         Color: Darker than Gray  
Pixel 2: z!!   RGB: 122,33,33        Color: Darker and Paler than Red  
Pixel 3: zz!   RGB: 122,122,33       Color: Darker and Paler than Yellow  
Pixel 4: zzz   RGB: 122,122,122      Color: Gray  
Pixel 5: !zz   RGB: 33,122,122       Color: Darker and Paler than Cyan  
Pixel 6: !!z   RGB: 33,33,122        Color: Darker and Paler than Blue  
Pixel 7: !z!   RGB: 33,122,33        Color: Darker and Paler than Green  
Pixel 8: z!z   RGB: 122,33,122       Color: Darker and Paler than Magenta  
Pixel 9: zzz   RGB: 122,122,122      Color: Gray  

![Example Image](https://lh3.googleusercontent.com/os7PrswZHl96cVFTyQTrqBaGt_Xyh6EyWuju8gWXtOP_RJiCOvwOc81h8GKvkuBIcGeuUaBe-xcQFddweLQmXPi-OIY3WSb2nUUvt0wXGWHNPE6gH9W2mAe9wKQZenaKaO6LJ5EZ2_il4DM1yJ1TvC5grRLX0zBtzoE3XxyqYx7uFneFBqVO7yqa_p7hRmB1LqqVaekQg9uIlAt3K8T2yiS2SMwdePybe8MPRsptgm718rLR8e7oekkV6YSvPbokCYipw7RhMLA6DMRidDRhjv-4wJSUIwwUy18DZKpA4qUadsA8ZAk5rS19blTLHs1JMlHVRm4KfqIeLjfnlk49rRegJmKv_zh0xeWM87zFzI2B27GLHQK5a9QH1p1CtOW8QhHaU1YEi-RI6KukBtRgAScvpr1sHxmQt9Jq4Y4xMv9kpqvVhe15jLlv9cOu5406z4WEz-h54a-Z5JOdKQijesaNoBQkrLM5g_7nwWYYZYUB2Fu4SuydcEI2EyV1BKC2SZhdapzQh1gBxAlwKc4UNUekKzyY2czemoGMdLnZ0NfbFdYvPyFUtbvCz2W9Da6kjTmLRbjoKicbfaabwWseI5tsK8mvd5zW1chRzCskIpWpQ25jWaPkNEv-yoMS_cft31nrgjXpyg63m1onMZiQwqpr-JGXEwqwQWQ6UTAlKe-1TDRymnqwneaRmo7chQ=w500-h400-no?authuser=0)
