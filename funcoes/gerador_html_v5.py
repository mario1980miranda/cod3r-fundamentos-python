BLOCO_ATRS = ('bloco_accesskey', 'bloco_id')
UL_ATRS = ('ul_id', 'ul_style')


def filtrar_atributos(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False,
              **novos_atributos):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args,
                                                            **novos_atributos)
    atributos = filtrar_atributos(novos_atributos, BLOCO_ATRS)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atributos):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul {filtrar_atributos(novos_atributos, UL_ATRS)}>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(inline=True, conteudo='inline', classe='info'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    print(tag_bloco(tag_lista, 'Sabado', 'Domingo',
                    classe='info', inline=True))
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo',
                    ul_id='lista', ul_blabla='abc'))
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo',
                    ul_id='lista', ul_style='color:red'))
