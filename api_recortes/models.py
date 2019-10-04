# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiApimodel(models.Model):

    class Meta:
        managed = False
        db_table = 'api_apimodel'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class RecortesCaderno(models.Model):
    arquivo = models.CharField(max_length=100)
    tribunal = models.CharField(max_length=200)
    data = models.DateField()
    nome = models.CharField(max_length=200)
    data_criacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'recortes_caderno'


class RecortesControle(models.Model):
    numeracao_unica = models.CharField(max_length=20)
    recorte = models.TextField()
    data_criacao = models.DateField()
    codigo_diario = models.CharField(max_length=200)
    ids_recortes_filhos = models.TextField()
    fonte = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recortes_controle'


class RecortesDiario(models.Model):
    data_criacao = models.DateField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    data_publicacao = models.DateTimeField()
    codigo_diario = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'recortes_diario'


class RecortesDownloaddiario(models.Model):
    nome_diario = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'recortes_downloaddiario'


class RecortesLinkIgnorado(models.Model):
    url = models.CharField(max_length=200)
    id_recorte = models.BigIntegerField()
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=254)
    motivo = models.TextField()
    nome = models.CharField(max_length=200)
    rg = models.CharField(max_length=20)
    data_criacao = models.DateTimeField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    remover_completamente = models.BooleanField()
    numeracao_unica = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'recortes_link_ignorado'


class RecortesLogcommanddownload(models.Model):
    comando = models.CharField(max_length=200)
    instancia_id = models.CharField(max_length=50, blank=True, null=True)
    log_text = models.TextField()
    finalizado = models.BooleanField()
    data_criacao = models.DateTimeField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    tempo_de_execucao = models.DecimalField(max_digits=8, decimal_places=4)
    parametros = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recortes_logcommanddownload'


class RecortesNomecaderno(models.Model):
    nome = models.CharField(max_length=500)
    codigo_caderno = models.CharField(max_length=500)
    data_criacao = models.DateTimeField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    diario = models.ForeignKey('RecortesNomediario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recortes_nomecaderno'
        unique_together = (('diario', 'codigo_caderno'),)


class RecortesNomediario(models.Model):
    nome = models.CharField(max_length=500)
    codigo_diario = models.CharField(max_length=500)
    segmento_judiciario = models.CharField(max_length=20, blank=True, null=True)
    tribunal = models.CharField(max_length=50, blank=True, null=True)
    data_criacao = models.DateTimeField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    estados = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recortes_nomediario'


class RecortesRecorte(models.Model):
    data_criacao = models.DateField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    numeracao_unica = models.CharField(max_length=20)
    recorte = models.TextField()
    data_publicacao = models.DateField()
    codigo_diario = models.CharField(max_length=200)
    caderno = models.CharField(max_length=200, blank=True, null=True)
    novo_recorte = models.BooleanField()
    paginas_diario = models.TextField(blank=True, null=True)
    nup_invalido = models.BooleanField(blank=True, null=True)
    nup_invalido_msg = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'recortes_recorte'


class RecortesRecorteStfStj(models.Model):
    data_criacao = models.DateTimeField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    numeracao_unica = models.CharField(max_length=20, blank=True, null=True)
    recorte = models.TextField()
    data_publicacao = models.DateTimeField()
    codigo_diario = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'recortes_recorte_stf_stj'


class RecortesRecorteTjmt(models.Model):
    data_criacao = models.DateTimeField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    numeracao_unica = models.CharField(max_length=40, blank=True, null=True)
    recorte = models.TextField()
    data_publicacao = models.DateTimeField()
    codigo_diario = models.CharField(max_length=200)
    caderno = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recortes_recorte_tjmt'


class RecortesRegistrodownloaddiario(models.Model):
    data = models.DateField()
    data_criacao = models.DateTimeField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    caderno = models.ForeignKey(RecortesNomecaderno, models.DO_NOTHING)
    quantidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recortes_registrodownloaddiario'
