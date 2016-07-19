from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional, Regexp
from app.model.cve import cve_ids_regex
from app.model.cvegroup import pkgver_regex, pkgname_regex
from app.model.enum import Status


class AddGroupForm(Form):
    cve = TextAreaField(u'CVE', validators=[DataRequired(), Regexp(cve_ids_regex)])
    pkgname = StringField(u'Package', validators=[DataRequired(), Regexp(pkgname_regex)])
    description = TextAreaField(u'Description', validators=[])
    affected = StringField(u'Affected version', validators=[DataRequired(), Regexp(pkgver_regex)])
    fixed = StringField(u'Fixed Version', validators=[Optional(), Regexp(pkgver_regex)])
    status = SelectField(u'Status', choices=[(e.name, e.label) for e in [*Status]], validators=[DataRequired()])
    bug_ticket = StringField('Bug ticket', validators=[])
    notes = TextAreaField(u'Notes', validators=[])
    submit = SubmitField(u'submit')
