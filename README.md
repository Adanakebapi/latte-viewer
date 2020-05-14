## Latte Viewer
Latte Viewer is a program to convert latte files to png files or image files to latte files.  
It supports JPG, JPEG and PNG files.  
You can convert latte files to only png format.  
**NOTE:** I'm NOT recommending using translucent files! Latte doesn't supports alpha value, your program can be CRASHED!

An Image file to Latte format  
![GUI_IMG1](https://lh3.googleusercontent.com/PHXBvDtEQ3nZaxl6tJsvxcPKMIq5S5eUXl_cAT2gyYeuHjrWzxXgo0OW2WZ1kgy3dJO-vV7nn9YYOPAxj_GqWbzYbs3Tza-KHvaITczVHP0R8fGVAqfbPgTcSYsn6YWdyRFt9ROjY0ajMRsxxKqcBxtSCiR-bWk23njyHrPf3j3oNFxbWYodZwu0g-ZD62ykaR1gh9x4qNRmGc4WqK1Vo_tz3Wp521_7GrQl-q4PGM75ML9trUiMDavsioj8kVjJuhV_D-bZujCIBrHAtHbcHYH9MSEBDhypvxc48SwICrSulGqu2tNX-UmV0-u15c1FV8wjB2QGovyib_M_RZam9lo0nKEpWB3KNMzRhq0IyIYAk-2nGgb0HDZyjakuGWgNRsl0SuXOeEP4rmAoP00EdugeRfFPthKxJkET0FmnLt0iSSi8eIFHaogNpmzLkNoSQ3vdSqn2Xz-w137MUpBH8lVhxGaXyM9-tAuiT0MviHZNZy3R0CszrQsJe92l-bO7WGdhdxgf3VBZqCEOQZblifuLKyyi659_kgGweQhzIO4U-bUox_6XBYiSRewFh-fZ13nwana3pGbBc0ebk6QV4wBHJ921PhTDfdYTXVP4a9jn_tMx1U-_fDIEU29z8A7xLz2LrfCYVQsXrKhhBxgxNpTu4-G4TpBd4dtIFUQ-BD-Pmugu4rkX6TwsuSSFp3eQKxILOLr-Atkx2dmXf-7dmv4OdLUzxXN2esm6ewwVFGOC0Q88MTnB9AU=w800-h524-no?authuser=0)  
  
A Latte file to Image format  
![GUI_IMG2](https://lh3.googleusercontent.com/zNRTL_He61DvxI_Nc9GyxirQTtSIBZiHUgrT5HLYTYINGPQ7o59D0KzdEpz6IbVfM5-hE8x7S6D-GwQ7gDCOgORSRkg1-DIQnPenw8-gDs4_ZDM9ZUjdMYuUDse2QBKg2q9sWSL0AmcL7PVCro9oClBOXbZGd0SviF_crppZJ8FFtZ_a9EKuQCC6yrqw6zmnbNxxE_xVmTuJWJgsOMw0gADOQKxFhVJAe_gnJhnszhN34Vt0n-bxrwJRP2FprAFydliF4cn7gMbt4TR5AMG6Tabl8Hy_RDx6msDEoCEHNzyMOkxOj0Yq6_tTLkW8qFX1hNhoD4TcpmjWeGgXsze3xQML9FEYTRAJqmDJb7yvxlgWiurrSCCfP6f19Ird1FCNPf75-uUgUgXgXSdlVKBEDNZMWJqkxOBdM5LKCk9XC_Ws09SsYmiVIec9by0rxQUtVkVjbYsBEZvQIaZNQEsxacpAFvPSwPl4VGKhpTFNISamLg4t4oE02oKGu8s9GxoUkX1ZRpsIxlXb20yIHuQRE2MqFXlnPPMl5ZL4Zv52HODVaDBlStZ-6-cN92Qv3SYYk1xmYb8f2GgCCZ9x9L5bRVxQZWO7G2GhPhozy2m49gmmhzvNS0GBcaahUCW-8w7nEAl4X0_VhWNxZyaRMP_T7JM9wSzoEpFContZZdhpMTge2okU09Gbn7c3GtxMgATJHEXqji_AfJQq63aC9jmXNF30QaxT5uuLxV--RgTNtifmrCPRd97dtQA=w800-h524-no?authuser=0)  
  
The listbox at top-left shows the .latte, .jpg, .jpeg and .png files in the same folder.  
The entry at top-right of listbox for browsing the file with path.  
The button at the right of the entry for browse the path.  
The button at middle-right of GUI for saving the file as .png or .latte file.  
The button at bottom of entry for browsing the file with explorer.

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

![Example Image](https://lh3.googleusercontent.com/NGkjNiwy70aEq_PMHj_rGsI7U6ogWzW9GQnEbwh9smmVT-zs1lKpUACiBGJLC9DH-aGQMWNVV1up2SFmz81a2NAI8um-zz_QCgsq6sB6ClU3gjZLcSZaKDl_Uy4FBsz7ji2vGkQDvGmey4jA0NKs0HSCjz1gl59g-0mqR2V6EOT_PoceWyDbAu-UKoed1pMz5dTFRdNcpZ1VA32LaHEdhIHbePdN165b7O8Q6n0xVRvBhqrwAYMM5GJlfQCLl73yrJtS_f7Kq1LxzcOShp2zZU63U3zr09oYHhaciC7sjapDS6w6cha9cYmLNcxv-L-X0MEWB2gpr8pgcHPcHePglbK9DAm0Ec6crfl1RwcJBeqidkCq0cFWF-3CNT0OHHDWk5AMMdK541Rdm8hERLa0b6A83aE9bSqE1ewh2aaZGX0-I-jfVYRllZAkPbB04-ovHAw16brtGmyVtWNSvY75lSb_PQ6NkJdV9MdR0F10GtRAUCM_b5kiwWkMg2vdL9UbNvMMUJ3JU4ZzAi1bzp5VhZIGVE-k536ev3ssdGWfI80eTUhtiinqryXq07XKozJi5DA5cGh9_FU0XZVlMu-C6rvWm1BreV_KqWOfu9xXQxSeEOMpMMgUI5BQz8DqsBLz3NG10TeOlRJcYb-PDWiQgnJpR5HfTRYGcD9_phvOW3iRN9ZCXTwzKtht9Udp7sIno_gRX1TIRX5BA4qCYm5qM0UbHBaAiXZl1fNr8ge-LkkPS4n13NgQbBM=w500-h400-no?authuser=0)
