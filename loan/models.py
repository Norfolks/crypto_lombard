from django.db import models

from accounts.models import User


class LoanProposal(models.Model):
    borrower = models.ForeignKey(User, related_name='borrower', blank=True, null=True,
                                 on_delete=models.SET_NULL)

    amount = models.CharField(max_length=100, verbose_name='amount')
    duration = models.DurationField(verbose_name='duration')
    percent = models.IntegerField(verbose_name='percent')
    asset = models.CharField(max_length=42, verbose_name='asset')
    token_id = models.CharField(max_length=100, verbose_name='token_id')


class Loan(models.Model):
    borrower = models.ForeignKey(User, related_name='borrower', blank=True, null=True,
                                 on_delete=models.SET_NULL)
    investor = models.ForeignKey(User, related_name='investor', blank=True, null=True,
                                 on_delete=models.SET_NULL)

    amount = models.CharField(max_length=100, verbose_name='amount')
    end_time = models.DateTimeField(verbose_name='end_date')
    percent = models.IntegerField(verbose_name='percent')
    asset = models.CharField(max_length=42, verbose_name='asset')
    token_id = models.CharField(max_length=100, verbose_name='token_id')
    address = models.CharField(max_length=42, verbose_name='address')


class ProposalAccept(models.Model):
    investor = models.ForeignKey(User, related_name='investor', on_delete=models.CASCADE)
    proposal = models.ForeignKey(LoanProposal, related_name='proposal', on_delete=models.CASCADE)
