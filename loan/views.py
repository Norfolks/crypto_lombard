from django.shortcuts import render
from django.views.generic import ListView

from loan.models import LoanProposal, Loan


def kitties_list(request):
    return


def create_proposal_view(request):
    return


class ProposalListView(ListView):
    model = LoanProposal
    template_name = ""
    paginate_by = 25

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', 'give-default-value')
        order = self.request.GET.get('orderby', 'give-default-value')
        return


def create_loan_view(request):
    return

class LoanListView(ListView):
    model = Loan
    template_name = ""
    paginate_by = 25

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', 'give-default-value')
        order = self.request.GET.get('orderby', 'give-default-value')
        return

