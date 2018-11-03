from django.shortcuts import redirect, render
from django.views import View

from entity.models import Member
from entity.forms import GroupApplicationForm


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class Apply(View):

    login_required = True
    def get(self, request):
        form = GroupApplicationForm()
        return render(request, 'group/apply.html', {'form': form})


    def post(self, request):
        form = GroupApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=True)

            # make the user the owner of the company
            member = Member.objects.create(
                entity=app,
                user=request.user,
                role=Member.Roles.OWNER
            )
            member.save()
            return redirect('/')