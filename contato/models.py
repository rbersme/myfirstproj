from django.db import models

class Cadastro(models.Model):

    SEXO_CHOICES=(
        (u'masculino', u'Masculino'),
        (u'feminino', u'Feminino')
    )

    ECIV_CHOICES = (
        (u'solteiro', u'Solteiro(a)'),
        (u'casado', u'Casado(a)'),
        (u'divorciado', u'Divorciado(a)'),
        (u'amasiado', u'Amasiado(a)'),
        (u'separado', u'Separado(a)'),
        (u'viuvo', u'Viúvo(a)'),
        (u'divorciado', u'Divorciado'),
    )

    UF_CHOICES=(
        (u'ac', u'AC'),
        (u'al', u'AL'),
        (u'am', u'AM'),
        (u'ap', u'AP'),
        (u'ba', u'BA'),
        (u'ce', u'CE'),
        (u'df', u'DF'),
        (u'es', u'ES'),
        (u'go', u'GO'),
        (u'ma', u'MA'),
        (u'mg', u'MG'),
        (u'ms', u'MS'),
        (u'mt', u'MT'),
        (u'pa', u'PA'),
        (u'pb', u'PB'),
        (u'pe', u'PE'),
        (u'pi', u'PI'),
        (u'pr', u'PR'),
        (u'rj', u'RJ'),
        (u'rn', u'RN'),
        (u'ro', u'RO'),
        (u'rr', u'RR'),
        (u'rs', u'RS'),
        (u'sc', u'SC'),
        (u'se', u'SE'),
        (u'sp', u'SP'),
        (u'to', u'TO')

    )

    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, unique = False, blank = False)
    est_civil = models.CharField(max_length=50, choices = ECIV_CHOICES, verbose_name='Estado Civil')
    sexo = models.CharField(max_length=50, choices = SEXO_CHOICES, null=True, blank = True)
    profissao = models.CharField(max_length=50, null=True, blank = True)
    cpfcnpj = models.CharField(max_length=30, null=True, blank = True)
    endereco = models.CharField(max_length=50, null=True, blank = True)
    bairro = models.CharField(max_length=50, null=True, blank = True)
    cidade = models.CharField(max_length=50, null=True, blank = True)
    cep = models.CharField(max_length=10, null=True, blank = True)
    uf = models.CharField(max_length=2, choices = UF_CHOICES, null=True, blank = True)
    telefone1 = models.CharField(max_length=40, null=True, blank = True)
    telefone2 = models.CharField(max_length=40, null=True, blank = True)
    email = models.CharField(max_length=150, null=True, blank = True)


