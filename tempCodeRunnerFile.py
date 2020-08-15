t.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        api.update_with_media(filename)
        os.remove(filename)
    else:
        tweet()
    sleep(120)