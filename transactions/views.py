from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

from django.views.generic.edit import FormView
from django.db.models.query import QuerySet

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from transactions.models import Transaction
from accounts.models import UserBankAccount
from .forms import DepositForm
from django.contrib.auth import update_session_auth_hash

from .constants import  ADD_BALANCE


from django.template.loader import render_to_string

# Create your views here.

# def send_transaction_email(user, amount, subject, template):
#         message = render_to_string(template, {
#             'user' : user,
#             'amount' : amount,
#             'subject':subject
#         })
#         send_email = EmailMultiAlternatives(subject, '', to=[user.email])
#         send_email.attach_alternative(message, "text/html")
#         send_email.send()

class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name='transactions/transaction_form.html'
    model=Transaction
    title=''
    success_url=reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs= super().get_form_kwargs()
        kwargs.update({
            'account':self.request.user.account,
        })
        return kwargs
    

    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'title':self.title
        })
        return context

class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Add Balance'

    def get_initial(self):
        initial = {'transaction_type': ADD_BALANCE}
        return initial

    def form_valid(self, form):
       

        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount 
        account.save(
            update_fields=[
                'balance'
            ]
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )

        # send_transaction_email(self.request.user, amount, "Deposite Message", "transactions/deposite_email.html")

        return super().form_valid(form)
    