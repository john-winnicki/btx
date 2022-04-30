from datetime import datetime
import os
from airflow import DAG
from plugins.jid import JIDSlurmOperator

# DAG SETUP
description='BTX detector distance estimation DAG'
dag_name = os.path.splitext(os.path.basename(__file__))[0]

dag = DAG(
    dag_name,
    start_date=datetime( 2022,4,1 ),
    schedule_interval=None,
    description=description,
  )


# Tasks SETUP
task_id='run_analysis'
run_analysis = JIDSlurmOperator( task_id=task_id, dag=dag)

task_id='opt_distance'
opt_distance = JIDSlurmOperator( task_id=task_id, dag=dag)

# Draw the DAG
run_analysis >> opt_distance
