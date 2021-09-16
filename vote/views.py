from django.shortcuts import render, get_object_or_404
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect


from .forms import ChoiceFormSet
from .models import *


def home(request):
    all_address_list = Address.objects.all()
    return render(request, 'vote/home.html', {'all_address_list': all_address_list})


class AddressChoiceCreate(CreateView):
    template_name = 'vote/add_address.html'
    model = Address
    fields = ['country', 'city', 'street', 'house', 'residents', 'question_text']
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        data = super(AddressChoiceCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['choices'] = ChoiceFormSet(self.request.POST)
        else:
            data['choices'] = ChoiceFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        choices = context['choices']
        with transaction.atomic():
            self.object = form.save()

            if choices.is_valid():
                choices.instance = self.object
                choices.save()
        return super(AddressChoiceCreate, self).form_valid(form)


def vote(request, address_id):
    address = get_object_or_404(Address, pk=address_id)
    try:
        selected_choice = address.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        return render(request, 'vote/vote.html', {
            'address': address,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('home'))
