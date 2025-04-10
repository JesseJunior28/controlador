from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'matricula', 'cargo', 'setor', 'is_plantonista', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('matricula', 'cargo', 'setor', 'telefone', 'is_plantonista')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Adicionais', {
            'classes': ('wide',),
            'fields': ('matricula', 'cargo', 'setor', 'telefone', 'is_plantonista')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
