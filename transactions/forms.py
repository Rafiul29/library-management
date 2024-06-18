from typing import Any
from django import forms
from .models import Transaction
from accounts.models import UserBankAccount

class TransactionFrom(forms.ModelForm):
    
    class Meta:
        model = Transaction
        fields = ['amount','transaction_type']

    def __init__(self,*args, **kwargs):
        self.account = kwargs.pop('account') # account value ke pop kore anlam
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True # ei field disable thakbe
        self.fields['transaction_type'].widget = forms.HiddenInput() # user er theke hide kora thakbe

    def save(self, commit=True):
        self.instance.account=self.account
        self.instance.balance_after_transaction=self.account.balance
        return super().save()


class DepositForm(TransactionFrom):
    def clean_amount(self): #amount field ke filter kora holo
        min_deposit_amount=100
        amount = self.cleaned_data.get('amount')

        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount}$'
            )
        return amount
    
# class WithdrawFrom(TransactionFrom):
#     def clean_amount(self):
#         account=self.account
#         min_withdraw_amount=500
#         max_withdraw_amount=20000
#         balance=account.balance
#         amount = self.cleaned_data.get('amount')

#         if amount <  min_withdraw_amount:
#             raise forms.ValidationError(
#                 f'You can withdraw at least {min_withdraw_amount} $'
#             )
#         if amount >  max_withdraw_amount:
#             raise forms.ValidationError(
#                  f'You can withdraw at most {max_withdraw_amount} $'
#             )
#         if amount >  balance:
#             raise forms.ValidationError(
#                  f'You have {balance} $ in your account. '
#                 'You can not withdraw more than your account balance'
#             )

#         return amount

# class LoanRequestForm(TransactionFrom):
#     def clean_amount(self):
#         amount = self.cleaned_data.get('amount')

#         return amount

# class TransferForm(TransactionFrom):
#     recipient_account = forms.IntegerField()


#     class Meta(TransactionFrom.Meta):
#         fields = TransactionFrom.Meta.fields + ['recipient_account']

#     def clean_amount(self):
#         amount = self.cleaned_data.get('amount')
#         account_number = self.cleaned_data.get('recipient_account')
#         if amount>self.account.balance:
#              raise forms.ValidationError("Insuficeinent balance")
#         return amount
    
#     def clean_recipient_account(self):
#         account_number = self.cleaned_data.get('recipient_account')
#         try:
#             findUserAccount = UserBankAccount.objects.get(account_no=account_number)
#         except UserBankAccount.DoesNotExist:
#             raise forms.ValidationError("Recipient account not found")
        
#         return account_number
    
