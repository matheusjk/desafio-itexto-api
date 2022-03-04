from app import create_app, db, func, datetime
import app


class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    version = db.Column(db.BigInteger, nullable=False)
    cliques = db.Column(db.Integer, nullable=False)
    data_inclusao = db.Column(db.DateTime(), default=func.localtimestamp(), nullable=False)
    data_publicacao = db.Column(db.DateTime(), default=func.localtimestamp())  # VOLTAR AQUI
    resumo = db.Column(db.String(200), nullable=False)
    site_id = db.Column(db.BigInteger, db.ForeignKey('site.id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)  # VOLTAR AQUI
    titulo = db.Column(db.String(128), nullable=False)
    url = db.Column(db.String(1024), nullable=False, unique=True)
    votos_negativos = db.Column(db.Integer, nullable=False)
    votos_positivos = db.Column(db.Integer, nullable=False)
    ativo = db.Column(db.Boolean(1), nullable=True, default=b'1')
    tentativas = db.Column(db.Integer, nullable=True, default=0)
    favoritos = db.Column(db.BigInteger, nullable=True)
    comentarios = db.Column(db.BigInteger, nullable=True)
    thumbnail = db.Column(db.String(1024), nullable=True)

    def __init__(self, version, cliques, site_id, resumo, titulo, url, votos_negativos, votos_positivos, ativo, tentativas,
                 favoritos, comentarios, thumbnail):
        self.version = version
        self.cliques = cliques
        self.site_id = site_id
        self.resumo = resumo
        self.titulo = titulo
        self.url = url
        self.votos_negativos = votos_negativos
        self.votos_positivos = votos_positivos
        self.ativo = ativo
        self.tentativas = tentativas
        self.favoritos = favoritos
        self.comentarios = comentarios
        self.thumbnail = thumbnail


class Site(db.Model):
    __tablename__ = "site"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    version = db.Column(db.BigInteger, nullable=False)
    ativo = db.Column(db.Boolean(1), nullable=False)
    autor_id = db.Column(db.BigInteger, db.ForeignKey('autor.id', ondelete="CASCADE", onupdate="CASCADE"),
                         nullable=False)
    endereco = db.Column(db.String(128), nullable=False, unique=True)  # VOLTAR AQUI
    nome = db.Column(db.String(128), nullable=False, unique=True)
    rss = db.Column(db.String(128), nullable=False, unique=True)
    sobre = db.Column(db.String(255), nullable=True, unique=True)
    tentativas = db.Column(db.Integer, nullable=True, unique=True, default=0)
    ultima_verificacao = db.Column(db.DateTime(), nullable=True)
    posts_dia = db.Column(db.Integer, nullable=True, default=-1)
    blog_post_id = db.relationship('BlogPost', backref='site', uselist=False)

    def __init__(self, version, ativo, autor_id, endereco, nome, rss, sobre, tentativas, ultima_verificacao, posts_dia):
        self.version = version
        self.ativo = ativo
        self.autor_id = autor_id
        self.endereco = endereco
        self.nome = nome
        self.rss = rss
        self.sobre = sobre
        self.tentativas = tentativas
        self.ultima_verificacao = ultima_verificacao
        self.posts_dia = posts_dia


class Autor(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(128), nullable=False)
    site_id = db.relationship("Site", backref="autor", uselist=False)

    def __init__(self, nome):
        self.nome = nome


