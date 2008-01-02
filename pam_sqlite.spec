%define name	pam_sqlite
%define version 0.3
%define release 4

Summary:	SQLite authentication for PAM
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		pam_sqlite-nullundeclared.patch
URL:		http://www.edin.dk/pam_sqlite/
License:	GPL
Group:		System/Libraries
BuildRequires:	pam-devel
BuildRequires:	sqlite-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
pam_sqlite allows developers to authenticate users against a table
in an SQLite database. It supports checking account information
(pam_acct_expired, new_authtok_reqd) and updating authentication
tokens. 

%prep
%setup -q
%patch0 -p 1 -b .nullundeclared

%build
%configure2_5x

%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}/lib/security
#install -d %{buildroot}%{_sysconfdir}/pam.d

install -m0755 pam_sqlite.so %{buildroot}/lib/security/pam_sqlite.so

#cat > %{buildroot}%{_sysconfdir}/pam.d/pam_sqlite <<EOF
#auth        required    pam_sqlite.so 
#account     required    pam_sqlite.so
#password    required    pam_sqlite.so
#EOF
#
#cat > %{buildroot}%{_sysconfdir}/pam_sqlite.conf <<EOF
#database = /etc/sysdb
#table = account
#user_column = user_name
#pwd_column = user_password
#expired_column = acc_expired
#newtok_column = acc_new_pwreq
#debug
#EOF

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc NEWS README
#%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam_sqlite.conf
#%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/pam_sqlite
%attr(0755,root,root) /lib/security/pam_sqlite.so


