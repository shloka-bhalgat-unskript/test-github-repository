from github import GithubException
from github import Github
import subprocess
# from github import GithubException
# from github import GithubException

# using an access token
g = Github("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")

#get branches for a user in a repo
# result = []
# user = g.get_user(login="shlokabhalgat")
# repos = user.get_repos()
# if len(list(repos))==0:
#     print([f"shloka-bhalgat-unskript does not have any repositories"]) 
# try:
#     for repo in repos:
#         if repo.full_name =="shlokabhalgat/poochshop":
#                 branches = repo.get_branches()
#                 [result.append(branch.name) for branch in branches[:100]]
# except GithubException as e:
#     if e.status== 403:
#         print("You need push access")
#         exit
#     else:
#         print(e.data)
#         exit
# print(result)


# result = []

# try:
#     user = g.get_user(login="shlokabhalgat")
#     repo = user.get_repos("shlokabhalgat/poochshop")
#     for branch in g.get_organization('orgName').get_repo('puppet').get_branches():
#     print (branch)
#     branches = repo.get_collaborators()
#     [result.append(branch.name) for branch in branches[:100]]
# except GithubException as e:
#     if e.status == 403:
#         print("You need push access")
#         exit
#     elif  e.status==404:
#         print("Incorrect username or repository")
#     else:
#         print("HERE")
#         print(e.data)
#         exit
# print(result)


#######get branch for a user in a repo
# result = []
# try:
#     user = g.get_user(login="shlokabhalgat")
#     repo = g.get_repo("shlokabhalgat/poochshop")
#     if repo.full_name =="shlokabhalgat/poochshop":
#         branch = repo.get_branch("bug-fex")
#         flag_to_check_branch = 0
#         if branch.name=="bug-fex":
#             flag_to_check_branch = 1
#             branch_info={}
#             branch_info["branch"] = branch.name
#             branch_info["commit"] = branch.commit.sha
#             result.append(branch_info)
#     if flag_to_check_branch==0:
#         print("Branch not found")
# except GithubException as e:
#     if e.status== 403:
#         print("You need push access")
#         exit
#     if e.status==404:
#         print("Incorrect username or repository")
#     else:
#         print(e.data)
#         exit
# print(result)


#delete a branch for a user in a repo
# result = []
# try:
#     user = g.get_user(login="shlokabhalgat")
#     repos = user.get_repos()
#     for repo in repos:
#         if repo.full_name =="shlokabhalgat/poochshop":
#             branches = repo.get_branches()
#             flag_to_check_branch = 0
#             for branch in branches:
#                 if branch.name=="reset-password":
#                     flag_to_check_branch = 1
#                     ref = repo.get_git_ref(f"heads/reset-password")
#                     print(ref)
#                     ref.delete()
#     if flag_to_check_branch==0:
#         print("Branch not found")
# except GithubException as e:
#     if e.status== 403:
#         print("You need push access")
#         exit
#     if e.status==404:
#         print("Incorrect username or repository")
#     else:
#         print(e.data)
#         exit
# print(result)

#list orgs for user
# result = []
# user = g.get_user(login="shloka-bhalgat-unskript")
# organizations = user.get_orgs()
# [result.append(o) for o in organizations]
# print(result)

# list repos for user
# result = []
# user = g.get_user(login="shloka-bhalgat-unskript")
# repos = user.get_repos()
# [result.append(repo.full_name) for repo in repos]
# print(result)

# list repos for team
# result = []
# try:
#     organization = g.get_organization("poochshop")
#     teams = organization.get_teams()
#     team = organization.get_team_by_slug("backeend")
#     repos = team.get_repos()
#     [result.append(repo.full_name) for repo in repos]
# except GithubException as e:
#     if e.status== 403:
#         print("You need admin access")
#         exit
#     elif e.status==404:
#         print("No such team or organization found")
#     else:
#         print(e.data)
#         exit
# print(result)


# list members in an org
# result = []
# organization = g.get_organization("unskript")
# members = organization.get_members()
# [result.append(member.login) for member in members]
# print(result)


#list teams in an org
# result = []
# organization = g.get_organization("poochshop")
# teams = organization.get_teams()
# try:
#     [result.append(team.name) for team in teams]
# except GithubException as e:
#     if e.status== 403:
#         print("You need admin access")
#         exit
# print(result)

########################################################get team in an org
# result = []
# try:
#     organization = g.get_organization("poochshop")
#     teams = organization.get_teams()
#     team = organization.get_team_by_slug("backend")
#     team_details = {}
#     team_details["team_name"] = team.name
#     team_details["team_id"] = team.id
#     team_details["members_count"]= team.members_count
#     team_details["repos_count"]= team.repos_count
#     team_details["privacy"]= team.privacy
#     team_details["permission"]= team.permission
#     result.append(team_details)
# except GithubException as e:
#     if e.status== 403:
#         print("You need admin access")
#         exit
#     elif e.status==404:
#         print("No such team found")
#     else:
#         print(e.data)
#         exit
# print(result)

# #list team projects
# result = []
# try:
# organization = g.get_organization("poochshop")
# teams = organization.get_teams()
# team = organization.get_team_by_slug("backend")
# team.add_to_repos
# repos = team.get_repos()
# for repo in repos:
#     print(repo)
#     projects = repo.get_projects()
# print(len(list(projects)))
# print([result.append(project) for project in projects])
# except GithubException as e:
#     if e.status== 403:
#         print("You need admin access")
#         exit
#     elif e.status==404:
#         print("No such team found")
#     else:
#         print(e.data)
#         exit
# print(result)

#create team
# result = []
# repo_names =[]
# list_of_repos = ''
# organization = g.get_organization("poochshop")
# repos = ["www"]
# for repo in repos:
#     list_of_repos  = organization.get_repo(repo)
# repo_names.append(list_of_repos)
# result = organization.create_team(name="test-team", repo_names=repo_names, privacy="closed", description="Test team for poochshop org")
# print(result)

# invite mem to org
# result = []
# organization = g.get_organization("unskript")
# team_name = 'backend'
# # TYPES OF ROLES= ["admin", "direct_member", "billing_manager"], TEAMS is ARRAY
# try:
#     teams = organization.get_teams()
#     for t in teams:
#         if t.name == team_name:
#             team = t
#     result = organization.invite_user(email="shlokabhalgat@gmail.com",
#             role="direct_member",
#             teams=[team])
# except Exception as error:
#     raise error
# if result is None:
#     print(f"Successfully sent invite")


# remove mem to org
# organization = g.get_organization("poochshop")
# try:
#     user = g.get_user('shloka-bhalgat-unskript')
#     mem_exist = organization.has_in_members(user)
#     if mem_exist:
#         result = organization.remove_from_members(user)
# except Exception as error:
#     raise error
# if result is None:
#     print(f"Successfully removed user")

#list collaborators for a repo
#must have push access to view a given repository collaborators
# repo_name = 'unskript/awesome-cloudops-automation'
# repo = g.get_repo(repo_name)
# collaborators = repo.get_collaborators()
# for collaborator in collaborators:
#     print(collaborator.login)

#list commits in a repo
# result = []
# repo_name = 'unskript/awesome-cloudops-automation'
# repo = g.get_repo(repo_name)
# commits = repo.get_commits()
# print(commits)
# for commit in commits:
#     commits_dict = {}
#     x = commit.author
#     if x is not None:
#         commits_dict["author"] = x.login
#         commits_dict["commit"]= commit.sha
#         result.append(commits_dict)
# print(result)

#list all repos in org
# result = []
# organization = g.get_organization("unskript")
# repos = organization.get_repos()
# [result.append(repo.full_name   ) for repo in repos]
# print(result)


# show pending invites
# should be admin
# result = []
# organization = g.get_organization("unskript")
# invites = organization.invitations()
# try:
#     [result.append(invite.login) for invite in invites]
# except GithubException as e:
#     if e.status== 403:
#         print("You need admin access")
#         exit
#     else:
#         print(e.data)
#         exit
# print(result)

#view all PR's
result = []
try:
    owner = g.get_user("shloka-bhalgat-unskript")
    repo_name = owner.login +'/'+ "test-github-repository"
    repo = g.get_repo(repo_name)
    prs = repo.get_pulls(state='open', sort='created', base='master')
    [result.append(pr.number) for pr in prs]
except GithubException as e:
    if e.status== 403:
        print("You need admin access")
        exit
    elif e.status==404:
        print("No such repository or user found")
    else:
        print(e.data)
        exit
print(result)












# Awesome-CloudOps-Automation