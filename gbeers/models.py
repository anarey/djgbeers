from django.db import models

# Create your models here.
ESTADO = (
        ('De', 'Deseo'),
        ('Pr', 'Propuesta'),
        ('Ac', 'Aceptada'),
        ('Re', 'Rechazada'),
        ('Ca', 'Cancelada'),
    )
TIPO_MULTI = (
        ('img','Imagen'),
        ('vid','Video'),
    )



class Usuario(models.Model):
    nombre = models.CharField(verbose_name="Nombre GNOME", max_length=30)
    twitter = models.CharField(verbose_name="Nombre Twitter", max_length=30)

class Sitio(models.Model):
    nombre_sitio = models.CharField(verbose_name="Sitio", max_length=30)
    direccion = models.CharField(verbose_name="Direccion", max_length=30)
    mapa = models.URLField()

class Entidad(models.Model):
    nombre = models.CharField(verbose_name="Entidad", max_length=30)
    web = models.URLField()
    twitter = models.CharField(verbose_name="Twitter entidad", max_length=30)

class Multimedia(models.Model):
    Multimedia = models.CharField(verbose_name="Descripcion multimedia", max_length=30)
    Enlace = models.URLField()
    tipo = models.CharField(verbose_name="Tipo de contenido", max_length=5,
            choices=TIPO_MULTI)
    
class Ponencia(models.Model):
    descripcion = models.CharField(verbose_name="Descripcion", max_length=200)
    ponente = models.ManyToManyField(Usuario, related_name='Ponente')
    estado = models.CharField(verbose_name="Estado", max_length=2, choices=ESTADO)
    multimedia = models.ManyToManyField(Multimedia, related_name='multimedia') 
    etiquetas = models.CharField(verbose_name="Etiquetas", max_length=20)

class Gbeers(models.Model):
    edicion = models.CharField(verbose_name="Edicion", max_length=200, null=False, blank=False)
    provincia = models.CharField(verbose_name="Provincia", max_length=20)
    ciudad = models.CharField(verbose_name="Ciudad", max_length=20)  # TODO Buscar modulo con las ciudades
    pais = models.CharField(verbose_name="Pais", max_length=20) ## TODO Enlazar con modulo
    ### Relacion 1 a muchso con usuarios.
    descripcion = models.CharField(verbose_name="Descripcion", max_length=1000) ## 
    contacto = models.ManyToManyField(Usuario)
    fecha = models.DateField()
    ## TODO hora
    into_sitio = models.ForeignKey(Sitio)
    ponencias = models.ManyToManyField(Ponencia,related_name='programa') 
    ### Propuestas y aceptadas.
    multimedia = models.ManyToManyField(Multimedia, related_name='multi')
    patrocina = models.ManyToManyField(Entidad, related_name='patrocina')
    organizadores = models.ManyToManyField(Entidad, related_name='Organiza')


