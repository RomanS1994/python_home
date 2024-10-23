class Person:
    name = None

    def greeting(self):
        print(f'I am {self.name}')

class Developer(Person):
    def do_job(self):
        print(f'I am writting code now...')


# junior = Developer()
# junior.name = 'Nike'
# junior.greeting()
# junior.do_job()


class Manager(Person):
    def manage(self):
        print('Deadline is coming, hurry up!')

class TeamLead(Developer, Manager):
    def manage(self):
        print('I am team lead')
        # return super().manage()


team_lead = TeamLead()
team_lead.name = 'Roman'
team_lead.greeting()
team_lead.do_job()
team_lead.manage()