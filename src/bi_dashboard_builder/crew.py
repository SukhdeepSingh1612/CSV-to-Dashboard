from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class DashboardBuilderCrew():
    """DashboardBuilderCrew for building a Business Intelligence dashboard"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def data_cleaner(self) -> Agent:
        return Agent(
            config=self.agents_config['data_cleaner'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=300,
            max_retry_limit=3,
        )

    @agent
    def insight_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['insight_generator'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=300,
            max_retry_limit=3,
        )

    @agent
    def chart_builder(self) -> Agent:
        return Agent(
            config=self.agents_config['chart_builder'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=300,
            max_retry_limit=3,
        )

    @agent
    def narrative_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['narrative_writer'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=300,
            max_retry_limit=3,
        )

    @agent
    def exporter(self) -> Agent:
        return Agent(
            config=self.agents_config['exporter'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=300,
            max_retry_limit=3,
        )

    @task
    def cleaning_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['cleaning_design_task']
        )

    @task
    def cleaning_code_task(self) -> Task:
        return Task(
            config=self.tasks_config['cleaning_code_task']
        )

    @task
    def eda_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['eda_design_task']
        )

    @task
    def eda_code_task(self) -> Task:
        return Task(
            config=self.tasks_config['eda_code_task']
        )

    @task
    def charts_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['charts_design_task']
        )

    @task
    def charts_code_task(self) -> Task:
        return Task(
            config=self.tasks_config['charts_code_task']
        )

    @task
    def narrative_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['narrative_design_task']
        )

    @task
    def narrative_code_task(self) -> Task:
        return Task(
            config=self.tasks_config['narrative_code_task']
        )

    @task
    def export_task(self) -> Task:
        return Task(
            config=self.tasks_config['export_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the BI dashboard builder crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
