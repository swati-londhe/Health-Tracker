from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HealthLog
from .forms import HealthLogForm

@login_required(login_url='/accounts/login/')
def health_logs(request):
    # ✅ Show only the current user's logs
    logs = HealthLog.objects.filter(user=request.user).order_by('-date')

    if request.method == 'POST':
        form = HealthLogForm(request.POST)
        if form.is_valid():
            health_log = form.save(commit=False)
            health_log.user = request.user  # ✅ Link log to the logged-in user
            health_log.save()
            return redirect('health_logs')
    else:
        form = HealthLogForm()

    return render(request, 'tracker/health_logs.html', {'form': form, 'logs': logs})
