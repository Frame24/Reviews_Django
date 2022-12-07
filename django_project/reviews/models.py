from django.db import models


class Classes(models.Model):
    id_class = models.AutoField(primary_key=True)
    class_name = models.CharField(db_column='class_name', max_length=50)
    
    def __str__(self):
        return self.class_name
    
    class Meta:
        managed = True
        db_table = 'classes'


class Texts(models.Model):
    id_text = models.AutoField(primary_key=True)
    text = models.TextField()
    classes = models.ManyToManyField(Classes, through='TextsClasses')
    
    def __str__(self):
        return self.text[:20] + "..."
    
    class Meta:
        managed = True
        db_table = 'texts'


class TextsClasses(models.Model):
    text_id = models.ForeignKey(Texts, models.DO_NOTHING, primary_key=True)
    class_id = models.ForeignKey(Classes, models.DO_NOTHING)
    

    class Meta:
        managed = True
        db_table = 'texts_classes'
        unique_together = (('text_id', 'class_id'),)


class TextsWords(models.Model):
    text_id = models.ForeignKey(Texts, models.DO_NOTHING, primary_key=True)
    word_id = models.ForeignKey('Words', models.DO_NOTHING)
    tfidf = models.FloatField()

    class Meta:
        managed = True
        db_table = 'texts_words'
        unique_together = (('text_id', 'word_id'),)


class Words(models.Model):
    id_word = models.AutoField(primary_key=True)
    word = models.CharField(max_length=50)
    
    def __str__(self):
        return self.word[:20] + "..."
    
    class Meta:
        managed = True
        db_table = 'words'


class WordsClasses(models.Model):
    word_id = models.ForeignKey(Words, models.DO_NOTHING, primary_key=True)
    class_id = models.ForeignKey(Classes, models.DO_NOTHING)
    vector = models.FloatField()

    class Meta:
        managed = True
        db_table = 'words_classes'
        unique_together = (('word_id', 'class_id'),)
