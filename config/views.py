from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "index.html")


class PanelView(AdminAccessMixin, View):

    def get(self, request, *args, **kwargs):
        # most_broadcast = WantAd.objects.annotate(want_count=Count("category")).order_by("-want_count").first()
        # user_count = user.objects.filter(is_admin=False).count()
        # want_ad_count = WantAd.objects.filter(confirmed=True).count()
        # category_count = Category.objects.count()
        # not_confirmed_count = WantAd.objects.filter(confirmed=False).count()
        # admin_count = user.objects.filter(is_admin=True).count()

        context = {
            # 'user_count': user_count,
            # 'category_count': category_count,
            # 'admin_count': admin_count,
            # 'most_broadcast': most_broadcast,
            # 'want_ad_count': want_ad_count,
            # 'not_confirmed_count': not_confirmed_count,

        }
        return render(request, 'config/panel.html')


class AboutUsView(AdminAccessMixin, View):
    def get(self, request):
        about_us = AboutUs.load()
        return render(request, 'config/about_us.html', {'about_us': about_us})


class RuleView(AdminAccessMixin, View):
    def get(self, request):
        about_us = Rule.load()
        return render(request, 'config/rule.html', {'rule': about_us})


class AboutUsCreateView(CreateView):
    model = AboutUs
    fields = ('description',)
    template_name = 'config/about_create.html'
    success_url = reverse_lazy("config:about_us")


class RuleCreateView(CreateView):
    model = Rule
    fields = ('description',)
    template_name = 'config/rule_create.html'
    success_url = reverse_lazy("config:rule")


class StaticView(AdminAccessMixin, View):
    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        want_ad = WantAd.objects.all()
        today_want_ad = want_ad.filter(created=jdatetime.date.today())
        not_confirmed = today_want_ad.filter(confirmed=False).count()
        month_want_ad = want_ad.filter(created__month=jdatetime.date.today().month).count()
        year_want_ad = want_ad.filter(created__year=jdatetime.date.today().year).count()
        special_want = want_ad.filter(express=True).count()
        top_city = want_ad.annotate(top_city=Count('city')).order_by('-top_city').first()
        top_date = want_ad.annotate(top_date=Count('created')).order_by('-created').first()
        top_zone = want_ad.annotate(top_zone=Count('zone')).order_by('-top_zone').first()
        paid = want_ad.filter(category__paid=True).count()
        parent_category = category.filter(parent=None).count()
        child_category = category.count() - parent_category
        context = {
            'today_want_ad': today_want_ad.count(),
            'month_want_ad': month_want_ad,
            'year_want_ad': year_want_ad,
            'special': special_want,
            'top_city': top_city,
            'top_zone': top_zone,
            'paid': paid,
            'not_confirmed': not_confirmed,
            'category_count': category.count(),
            'parent_category': parent_category,
            'child_category': child_category,
            'top_date': top_date,
        }
        return render(request, "config/static.html", context)
