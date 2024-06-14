from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session

from models.sujet import Sujet
from models.question import Question
from models.reponse import Reponse
from config.utils import is_logged_in

faq_blueprint = Blueprint('faq', __name__, url_prefix="/faq")


@faq_blueprint.route("/")
@is_logged_in
def faq_index():
    return render_template(
        "faq/index.html",
        sujets=Sujet.read_all(),
        question_read_all=Question.read_all,
        reponse_read_all=Reponse.read_all
    )


@faq_blueprint.route("/sujet/details/<sujet_id>")
@is_logged_in
def faq_sujets_details(sujet_id):
    sujet = Sujet.read_one(sujet_id)
    if not sujet:
        flash("Sujet non trouvée", "danger")
        return redirect(url_for('faq.faq_index'))

    return render_template(
        "faq/details.html", sujet=sujet, questions=Question.read_all(sujet_id), reponses=Reponse.read_all(sujet_id)
    )


@faq_blueprint.route("/sujet/create", methods=['GET', 'POST'])
@is_logged_in
def faq_sujets_create():
    if request.method == 'POST':

        text = request.form['text']

        if Sujet.find_exist(text):
            flash('Sujet déja existe', 'danger')
            return redirect(url_for('faq.faq_sujets_create'))
        else:
            Sujet.create(text)
            flash('Sujet ajoutée avec succés', 'success')
            return redirect(url_for('faq.faq_index'))

    return render_template(
        "faq/create.html"
    )


@faq_blueprint.route("/sujet/update/<sujet_id>", methods=['GET', 'POST'])
@is_logged_in
def faq_sujets_update(sujet_id):
    sujet = Sujet.read_one(sujet_id)
    if not sujet:
        flash("Sujet non trouvée", "danger")
        return redirect(url_for('faq.faq_index'))

    if request.method == 'POST':

        text = request.form['text']

        if Sujet.find_exist(text):
            flash('Sujet déja existe', 'danger')
            return redirect(url_for('faq.faq_sujets_create'))
        else:
            Sujet.update(sujet_id, text)
            flash('Sujet modifiée avec succés', 'success')
            return redirect(url_for('faq.faq_index'))

    return render_template(
        "faq/update.html", sujet=sujet
    )


@faq_blueprint.route("/sujet/delete/<sujet_id>")
@is_logged_in
def faq_sujets_delete(sujet_id):
    sujet = Sujet.read_one(sujet_id)
    if not sujet:
        flash("Sujet non trouvée", "danger")
        return redirect(url_for('faq.faq_index'))

    Sujet.delete(sujet_id)
    flash("Sujet supprimée avec succés", "success")
    return redirect(url_for('faq.faq_index'))


#########################################################################################################################
# Questions

@faq_blueprint.route("/sujet/details/<sujet_id>/questions/create", methods=['GET', 'POST'])
@is_logged_in
def faq_questions_create(sujet_id):
    sujet = Sujet.read_one(sujet_id)
    if not sujet:
        flash("Sujet non trouvée", "danger")
        return redirect(url_for('faq.faq_index'))

    if request.method == 'POST':

        text = request.form['text']

        if Question.find_exist(text):
            flash('Question déja existe', 'danger')
            return redirect(url_for('faq.faq_questions_create', sujet_id=sujet_id))
        else:
            Question.create(sujet_id, text)
            flash('Question ajoutée avec succés', 'success')
            return redirect(url_for('faq.faq_sujets_details', sujet_id=sujet_id))

    return render_template(
        "faq/questions/create.html", sujet_id=sujet_id
    )


@faq_blueprint.route("/sujet/details/<sujet_id>/questions/update/<question_id>", methods=['GET', 'POST'])
@is_logged_in
def faq_questions_update(sujet_id, question_id):
    sujet = Sujet.read_one(sujet_id)
    if not sujet:
        flash("Sujet non trouvée", "danger")
        return redirect(url_for('faq.faq_index'))

    question = Question.read_one(question_id)
    if not question:
        flash("Question non trouvée", "danger")
        return redirect(url_for('faq.faq_sujets_details', sujet_id=sujet_id))

    if request.method == 'POST':

        text = request.form['text']

        Question.update(question_id, text)
        flash('Question ajoutée avec succés', 'success')
        return redirect(url_for('faq.faq_sujets_details', sujet_id=sujet_id))

    return render_template(
        "faq/questions/update.html", sujet_id=sujet_id, question=question
    )


@faq_blueprint.route("/sujet/details/<sujet_id>/questions/delete/<question_id>")
@is_logged_in
def faq_questions_delete(sujet_id, question_id):
    sujet = Sujet.read_one(sujet_id)
    if not sujet:
        flash("Sujet non trouvée", "danger")
        return redirect(url_for('faq.faq_index'))

    question = Question.read_one(question_id)
    if not question:
        flash("Question non trouvée", "danger")
        return redirect(url_for('faq.faq_sujets_details', sujet_id=sujet_id))

    Question.delete(question_id)
    flash("Question supprimée avec succés", "success")
    return redirect(url_for('faq.faq_sujets_details', sujet_id=sujet_id))

#########################################################################################################################

#########################################################################################################################
# Reponses


@faq_blueprint.route("/sujet/details/<sujet_id>/reponses/create", methods=['GET', 'POST'])
@is_logged_in
def faq_reponses_create(sujet_id):
    sujet = Sujet.read_one(sujet_id)
    if not sujet:
        flash("Sujet non trouvée", "danger")
        return redirect(url_for('faq.faq_index'))

    if request.method == 'POST':

        text = request.form['text']

        if Reponse.find_exist(text):
            flash('Reponse déja existe', 'danger')
            return redirect(url_for('faq.faq_reponses_create', sujet_id=sujet_id))
        else:
            Reponse.create(sujet_id, text)
            flash('Reponse ajoutée avec succés', 'success')
            return redirect(url_for('faq.faq_sujets_details', sujet_id=sujet_id))

    return render_template(
        "faq/reponses/create.html", sujet_id=sujet_id
    )


@faq_blueprint.route("/sujet/details/<sujet_id>/reponses/update/<reponse_id>", methods=['GET', 'POST'])
@is_logged_in
def faq_reponses_update(sujet_id, reponse_id):
    sujet = Sujet.read_one(sujet_id)
    if not sujet:
        flash("Sujet non trouvée", "danger")
        return redirect(url_for('faq.faq_index'))

    reponse = Reponse.read_one(reponse_id)
    if not reponse:
        flash("Reponse non trouvée", "danger")
        return redirect(url_for('faq.faq_sujets_details', sujet_id=sujet_id))

    if request.method == 'POST':

        text = request.form['text']

        Reponse.update(reponse_id, text)
        flash('Reponse ajoutée avec succés', 'success')
        return redirect(url_for('faq.faq_sujets_details', sujet_id=sujet_id))

    return render_template(
        "faq/reponses/update.html", sujet_id=sujet_id, reponse=reponse
    )


@faq_blueprint.route("/sujet/details/<sujet_id>/reponses/delete/<reponse_id>")
@is_logged_in
def faq_reponses_delete(sujet_id, reponse_id):
    sujet = Sujet.read_one(sujet_id)
    if not sujet:
        flash("Sujet non trouvée", "danger")
        return redirect(url_for('faq.faq_index'))

    reponse = Reponse.read_one(reponse_id)
    if not reponse:
        flash("Reponse non trouvée", "danger")
        return redirect(url_for('faq.faq_sujets_details', sujet_id=sujet_id))

    Reponse.delete(reponse_id)
    flash("Reponse supprimée avec succés", "success")
    return redirect(url_for('faq.faq_sujets_details', sujet_id=sujet_id))

#########################################################################################################################
