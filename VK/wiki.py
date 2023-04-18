import wikipedia

def get_article(article):
    wikipedia.set_lang("ru")
    try:
        page = wikipedia.page(article) # чтобы найти статью на википедии
        return f'{page.url}\n{wikipedia.summary(article)[:900]}'
    except:
        return f"не удалось найти информацию"