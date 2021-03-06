# Alfred Workflows

Custom [workflows](https://www.alfredapp.com/workflows/) for [Alfred](https://www.alfredapp.com/).

![Alfred Logo](alfred-logo.png)

## endor

It's a very customized workflow to monitor a remote server. It's launched with `endor` keyword and it shows some information about the remote machine:

- CPU frequency.
- Memory usage.
- Disk usage.
- CPU load.

![Endor screen-recording](endor/img/endor.gif)

> I know it's quite difficult to adapt it to common cases since it's based on a concrete API.

[Take a look of this workflow!](endor)

## vip

Show information about networking:

- Local IP.
- Public IP.
- MAC address.

![VIP screen-recording](vip/img/vip.gif)

[Take a look of this workflow!](vip)

## bitly

Shorten url from clipboard using bitly.com API. Resulting url is also copied to the clipboard.

![Bitly screen-recording](bitly/img/bitly.gif)

[Take a look of this workflow!](bitly)

## translate

Translations between Spanish & English through library [py-googletrans](https://github.com/ssut/py-googletrans).

![Translate screen-recording](translate/img/translate.gif)

[Take a look of this workflow!](translate)

## ciap

Calculate the final price of an Amazon product if it were delivered to Canary Islands.

![CIAP screen-recording](ciap/img/ciap.gif)

[Take a look of this workflow!](ciap)

## savetweetvid

Download the video (as url) from a tweet url that it's already in the clipboard. Resulting downloaded video is shown on the browser and also copied to the clipboard.

![savetweetvid screen-recording](savetweetvid/img/savetweetvid.gif)

[Take a look of this workflow!](savetweetvid)

## photoroom

Remove background of selected images (in Finder) through the [PhotoRoom API](https://photoroom.com/api).

![photoroom screen-recording](photoroom/img/photoroom.gif)

[Take a look of this workflow!](photoroom)

## cleanurl

Remove tracking and extra query params from URLs.

For example:

https://es.aliexpress.com/item/1005001835574685.html?spm=a2g0o.productlist.0.0.588a497b7V3uQR&algo_pvid=8f2e3d27-536c-49e7-9e4e-cb190b6fc3a1&algo_exp_id=8f2e3d27-536c-49e7-9e4e-cb190b6fc3a1-0

👇🏻

https://es.aliexpress.com/item/1005001835574685.html

> IMPORTANT: This is not "smart" at all. Use it carefully since it only remove the rest of the URL after the ? sign.
