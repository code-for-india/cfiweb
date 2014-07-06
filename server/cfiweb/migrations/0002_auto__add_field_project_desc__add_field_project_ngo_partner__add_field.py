# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.desc'
        db.add_column(u'cfiweb_project', 'desc',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True),
                      keep_default=False)

        # Adding field 'Project.ngo_partner'
        db.add_column(u'cfiweb_project', 'ngo_partner',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True),
                      keep_default=False)

        # Adding field 'Project.ngo_poc'
        db.add_column(u'cfiweb_project', 'ngo_poc',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True),
                      keep_default=False)

        # Adding field 'Project.cfi_poc'
        db.add_column(u'cfiweb_project', 'cfi_poc',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True),
                      keep_default=False)

        # Adding field 'Project.members'
        db.add_column(u'cfiweb_project', 'members',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.desc'
        db.delete_column(u'cfiweb_project', 'desc')

        # Deleting field 'Project.ngo_partner'
        db.delete_column(u'cfiweb_project', 'ngo_partner')

        # Deleting field 'Project.ngo_poc'
        db.delete_column(u'cfiweb_project', 'ngo_poc')

        # Deleting field 'Project.cfi_poc'
        db.delete_column(u'cfiweb_project', 'cfi_poc')

        # Deleting field 'Project.members'
        db.delete_column(u'cfiweb_project', 'members')


    models = {
        u'cfiweb.project': {
            'Meta': {'object_name': 'Project'},
            'cfi_poc': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'ngo_partner': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'ngo_poc': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'})
        }
    }

    complete_apps = ['cfiweb']