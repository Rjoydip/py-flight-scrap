# py-flight-scrap

> 

## Running Locally

```sh
$ git clone https://github.com/Rjoydip/py-rubygarage-scrap.git # or clone your own fork
$ cd py-rubygarage-scrap
```

Download depedency `bs4` and `requests`

## Command line

The argument value `-p` or `-page`. Default page number is `one`.

```sh
python ./main.py -page 1
```

## Output

Structure the output json of a tag.

```
{
    'logo': '<tag logo>', 
    'link': '<tag original link>', 
    'title': '<tag title>', 
    'tag': {
        'name': '<tag name>', 
        'link': '<tag catrgory link>', 
        'views': '<number of viewers of that tag>'
    }
}
```
