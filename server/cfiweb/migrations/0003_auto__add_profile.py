# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'cfiweb_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512, null=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=512, null=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=512, null=True)),
            ('skills', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
            ('fb_id', self.gf('django.db.models.fields.CharField')(max_length=512, null=True)),
            ('linkedin_id', self.gf('django.db.models.fields.CharField')(max_length=512, null=True)),
            ('github_id', self.gf('django.db.models.fields.CharField')(max_length=512, null=True)),
        ))
        db.send_create_signal(u'cfiweb', ['Profile'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'cfiweb_profile')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'cfiweb.profile': {
            'Meta': {'object_name': 'Profile'},
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'github_id': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin_id': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'cfiweb.project': {
            'Meta': {'object_name': 'Project'},
            'cfi_poc': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'ngo_partner': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'ngo_poc': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cfiweb']