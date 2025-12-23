from flask import Blueprint, request, render_template, redirect, url_for
from database import SessionLocal
from models import Task
from enums import TaskPriority, TaskStatus

task_routes = Blueprint('task_routes', __name__)

def serialize_task(task):
    return{
        'id': task.id,
        'title':task.title,
        'description': task.description,
        'status':task.status,
        'priority': task.priority,
        'due_date': task.due_date,
        'created_at': task.created_at.isoformat()if task.created_at else None,
        'updated_at': task.updated_at
    }

@task_routes.route('/')
@task_routes.route('/home')
def home():
    session = SessionLocal()
    try:
        tasks = session.query(Task).all()
        return render_template('index.html', tasks=tasks)
    except Exception as e:
        return render_template('error.html',error=str(e))
    finally:
        session.close()

@task_routes.route('/create', methods=['GET'])
def create_task_page():
    return render_template('create_task.html')


@task_routes.route('/create', methods=['POST'])
def create_task():
    session = SessionLocal()
    try:
        title = request.form.get('title')
        description = request.form.get('description')  
        status = request.form.get('status', TaskStatus.pending)
        priority = request.form.get('priority', TaskPriority.moderate)
        due_date = request.form.get('due_date') or None  
        
        if not title:
            return render_template('create_task.html', error='Title is required')
        
        new_task = Task(
            title=title,
            description=description,
            status = TaskStatus(request.form.get('status', TaskStatus.pending.value)),
            priority = TaskPriority(request.form.get('priority', TaskPriority.moderate.value)),
            due_date=due_date
        )
        
        session.add(new_task)
        session.commit()

        return redirect(url_for('task_routes.home'))
    except Exception as e:
        session.rollback()
        return render_template('create_task.html',error=str(e))
    finally:
        session.close()

@task_routes.route('/task/<int:task_id>')
def view_task(task_id):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            return render_template('error.html', error = 'Task not found'), 404
        return render_template('view_task.html', task=task)
    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        session.close()

@task_routes.route('/edit/<int:task_id>', methods=['GET'])
def edit_task_page(task_id):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first() 
        if not task:
            return render_template('error.html', error='Task not found'), 404
        return render_template('edit_task.html', task=task)
    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        session.close()


@task_routes.route('/edit/<int:task_id>', methods=['POST'])
def update_task(task_id):
    session=SessionLocal()
    try:
        task = session.query(Task). filter(Task.id == task_id).first()
        if not task:
            return render_template('error.html',error='Task not found'),404
        
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        task.status = request.form.get('status')
        task.status = TaskStatus(request.form.get('status'))
        task.priority = TaskPriority(request.form.get('priority'))


        session.commit()

        return redirect(url_for('task_routes.view_task', task_id = task_id))
    except Exception as e:
        session.rollback()
        return render_template('error.html', error = str(e))
    finally:
        session.close()

@task_routes.route('/delete/<int:task_id>', methods = ['POST'])
def delete_task(task_id):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            return render_template('error.html', error='Task not found'),404
        
        session.delete(task)
        session.commit()

        return redirect(url_for('task_routes.home'))
    except Exception as e:
        session.rollback()
        return render_template('error.html')
    finally:
        session.close()


