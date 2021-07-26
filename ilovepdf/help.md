# Help

## Available tools

Reference: https://developer.ilovepdf.com/docs/api-reference

- `compress`
- `imagepdf`
- `merge`
- `officepdf`
- `pagenumber`
- `pdfa`
- `pdfjpg`
- `split`
- `unlock`
- `rotate`

## `split`

Use cases:

- `ranges 1,5,10-14` (split file following given page intervals)
- `fixed_range 2` (split file every 2 pages)
- `remove_pages 1,4,8-12,16` (remove pages following given intervals)

## `rotate`

Use cases:

- `rotate 90` (rotate all pages 90 degrees)
- `rotate 180` (rotate all pages 180 degrees)
- `rotate 270` (rotate all pages 270 degrees)