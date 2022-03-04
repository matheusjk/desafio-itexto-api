from app import redirect, url_for, Blueprint, datetime, jsonify
from app.models.tables import BlogPost, Autor, Site
import timeit


api = Blueprint('api', __name__, template_folder='templates', url_prefix="/api")


@api.route('/post/<string:busca>', methods=['GET'])
def buscaPorTexto(busca):
    try:
        listaBlogPost = []
        buscaPalavra = "%{}%".format(busca)
        blog = BlogPost.query.filter(BlogPost.titulo.like(buscaPalavra) | (BlogPost.resumo.like(buscaPalavra))).all()
        
        # blog = BlogPost.query.all()
        
        # site = Site.query.all()

        for linha in blog:

            listaBlogPost.append({
                "id": linha.id,
                "titulo": linha.titulo,
                "resumo": linha.resumo,
                "cliques": linha.cliques,
                "dataInclusao": linha.data_inclusao,
                "dataPublicacao": linha.data_publicacao,
                "votosPositivos": linha.votos_positivos,
                "votosNegativos": linha.votos_negativos,
                "favoritos": linha.favoritos,
                "comentarios": linha.comentarios,
                "url": 0,
                "blog": {
                    "id": linha.site.id,
                    "nome": linha.site.nome,
                    "resumo": linha.site.sobre,
                    "url": linha.site.endereco,
                    "ativo": linha.site.ativo,
                    "autor": {
                        "id": linha.site.autor.id,
                        "nome": linha.site.autor.nome
                    }

                }
            })


        # for linha in site:

        #     listaBlogPost.append({
        #         "endereco": linha.endereco
        #     })

        # return jsonify({'site': listaBlogPost})
        
        return jsonify({'blog': listaBlogPost})

    except Exception as error:
        print("Error ao executar metodo buscaPorTexto {}".format(error))
        

    
@api.route("/post/clique/<int:id>", methods=["GET"])
def buscaPorId(id):
    try:
        lista = []
        # buscaId = "%{}%".format(id)


        blog = BlogPost.query.filter_by(id=id).all()   

        inicio = timeit.default_timer()
        print(blog)

        for linha in blog:
    
            lista.append({
                "id": linha.id,
                "titulo": linha.titulo,
                "resumo": linha.resumo,
                "cliques": linha.cliques,
                "dataInclusao": linha.data_inclusao,
                "dataPublicacao": linha.data_publicacao,
                "votosPositivos": linha.votos_positivos,
                "votosNegativos": linha.votos_negativos,
                "favoritos": linha.favoritos,
                "comentarios": linha.comentarios,
                "url": linha.url,
                "blog": {
                    "id": linha.site.id,
                    "nome": linha.site.nome,
                    "resumo": linha.site.sobre,
                    "url": linha.site.endereco,
                    "ativo": linha.site.ativo,
                    "autor": {
                        "id": linha.site.autor.id,
                        "nome": linha.site.autor.nome
                    }

                }
            })

        fim = timeit.default_timer()
        print("TEMPO: {}".format(fim - inicio))
        return jsonify(lista)

    except Exception as error:
        print("Erro ao executar metodo buscaId {}".format(error))

