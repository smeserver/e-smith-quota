Summary: e-smith server and gateway - quota module
%define name e-smith-quota
Name: %{name}
%define version 1.10.0
%define release 5
Version: %{version}
Release: %smerelease %{release}
Packager: %{_packager}
License: GPL
Group: System Environment/Base
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-quota-1.10.0.sort.patch
Patch1: e-smith-quota-1.10.0-UntaintAccountName.patch
Patch2: e-smith-quota-1.10.0-Limits.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base >= 4.9.129, quota >= 3, perl-Quota
Requires: e-smith-lib >= 1.13.1
BuildRequires: e-smith-devtools >= 1.11.0-03, e-smith-test >= 0.1.12
AutoReqProv: no

%description
e-smith server and gateway software - quota module.

%changelog
* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Sun Jul 16 2006 Charlie Brady <charlie_brady@mitel.com> 1.10.0-04
- Fix sanity checking of hard/soft quota values, and fix "no limit" display
  text (fixes thanks to Robert van den Aker). [SME: 1462]

* Sun Jul 16 2006 Gavin Weight <gweight@gmail.com> 1.10.0-03
- Fix quota.pm to allow account names with ".". [SME: 1702]

* Mon May 01 2006 Charlie Brady <charlie_brady@mitel.com> 1.10.0-02
- Fix mis-sorting of users in quota table. [SME: 1346]

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.10.0-01
- Roll stable stream version. [SME: 1016]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.9.2-05
- Bump release number only

* Thu Oct 20 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.2-04]
- Add line break to over-quota email message to improve readability.

* Wed Oct 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.2-03]
- Re-fix L10N in over-quota warning messages. [SF: 1312830]

* Tue Oct 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.2-02]
- In warnquota, give Text::Template::fill_in an aliased reference to
  $conf, rather than a copy. [SF: 1312772]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.9.2-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.9.1-01]
- New dev stream before relocating L10Ns

* Tue Oct  4 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-14]
- Fix L10N in over-quota warning messages. [SF: 1312830]

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-13]
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-12]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-11]
- Update to current db access APIs (patches by Shad and Charlie) [SF: 1216546]

* Wed Jul 13 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-10]
- Add quota setup in fstab templates (moved from e-smith-base).

* Mon Jun 27 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-09]
- Really fix permissions of /etc/cron.d/warnquota. [SF: 1226700]

* Fri Jun 24 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-08]
- Make perms of /etc/cron.d/warnquota acceptible to latest crond.
  [SF: 1226700]

* Thu Mar 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-07]
- Fix some perl anachronisms which elicit warnings. [MN00075093]

* Thu Mar 10 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-06]
- Update success and error messages to use new convention
  (patch submitted by Shad Lords).

* Wed Dec 29 2004 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-05]
- Remount / with quota support before trying to create quota
  files. [MN00061221]

* Fri Dec 24 2004 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-04]
- Fix rc.quota_create's check for existing quota file, and add
  convertquota calls, in case of old style quota files.
  [MN00061221]

* Thu Dec 16 2004 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-03]
- Run /etc/rc.d/rc.quota_create before rc.sysinit, to enable
  filesystem quota support. [charlieb MN00061221]

* Wed Nov 10 2004 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-02]
- Untaint acct before using in system(). [charlieb MN00050161]

* Wed Nov 10 2004 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-01]
- Changing version to development stream number - 1.9.0

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Changing version to stable stream number - 1.8.0

* Tue Jun 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-22]
- Spanish nav bar [gordonr 9153]

* Fri May 30 2003 Mark Knox <markk@e-smith.com>
- [1.7.0-21]
- Whoops. Don't need /usr/lib/e-smith-quota anymore. Removed [markk 8847]

* Fri May 30 2003 Mark Knox <markk@e-smith.com>
- [1.7.0-20]
- Create template output dir in %build, and fragments need Locale::gettext 
  [markk 8847]

* Fri May 30 2003 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-19]
- Move fstab fragment into e-smith-base. [charlieb 8868]

* Tue May  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-18]
- Add Spanish lexicon for quota [lijied 3793]

* Thu Apr 17 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-17]
- Standardize the Add/Remove/Save button name [lijied 7921]

* Thu Apr 10 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-16]
- Change $q->table back [lijied 8034]

* Fri Apr  4 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-15]
- Change $q->table to $q->start_table where necessary [lijied 8034]

* Thu Apr  3 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-14]
- Removed SME Server branding [lijied 8016]

* Fri Mar 28 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-13]
- Modified /po/fr_CA to fr [lijied 6787]

* Fri Mar 28 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-12]
- Modified French lexicon to use lang="fr", rename the lexicon
  directory to fr [lijied 6787]

* Mon Mar 10 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-11]
- Modified charset tag in .po file [lijied 3930]

* Fri Mar  7 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-10]
- Modified en-us and fr-ca panel title
  modified en-us and fr-ca nav bar label [lijied 7356]
- Modified e-smith-devtools version [lijied 7578]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-09]
- Modified quotas panel order [lijied 7356]
- Added French .po file to po/fr_CA, and modified the
  %build in spec file  [lijied 7442]

* Tue Mar  4 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-08]
- Split en-us lexicon from quota panel [lijied 4030]

* Mon Mar  3 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-07]
- Added French lexicon for quota. [lijied 5003]

* Sat Jan 25 2003 Mike Dickson <miked@e-smith.com>
- [1.7.0-06]
- added ACTION to the lexicon [miked 6363]

* Wed Jan  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-05]
- Rewrote templates to use esmith::I18N [gordonr 5212]

* Fri Dec 27 2002 Mike Dickson <miked@e-smith.com>
- [1.7.0-04]
- minor UI update [miked 5494]

* Mon Dec  9 2002 Mike Dickson <miked@e-smith.com>
- [1.7.0-03]
- updates for new UI [miked 5494]

* Thu Nov 21 2002 Mike Dickson <miked@e-smith.com>
- [1.7.0-02]
- update to new UI system [miked 5494]

* Wed Nov 20 2002 Mike Dickson <miked@e-smith.com>
- [1.7.0-01]
- Changing to development stream; version upped to 1.7.0

* Wed Oct 16 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.6.1-03]
- Don't suppress quota warnings if hard limit is zero [gordonr 5230]

* Tue Oct 15 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.1-02]
- Fix I18N of From header in warning emails. Quote "full name"
  part of From header (to be sure). [charlieb 5205]

* Tue Oct 15 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.1-01]
- Fix use of comma as string concat operator in overquota mail message
  templates. Break some long lines while we are at it. [charlieb 5178]

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Roll to maintained version number to 1.6.0

* Fri Oct 11 2002 Mark Knox <markk@e-smith.com>
- [1.5.3-03]
- Improved unit suffix handling to more closely correspond to docs [markk 5102]
- Allow "unlimited" hard quota with soft quota [markk 5102]

* Tue Oct  8 2002 Mark Knox <markk@e-smith.com>
- [1.5.3-02]
- Improved error strings [markk 5102]

* Wed Sep 25 2002 Mark Knox <markk@e-smith.com>
- [1.5.3-01]
- Rolled version to clean up patch errors

* Wed Sep 25 2002 Mark Knox <markk@e-smith.com>
- [1.5.2-04]
- Clean up panel display and instructions [markk 4475]

* Wed Sep  4 2002 Mark Knox <markk@e-smith.com>
- [1.5.2-03]
- Disambiguated the explanation of how disk usage is calculated. [markk 4473]

* Tue Aug 27 2002 Mark Knox <markk@e-smith.com>
- [1.5.2-02]
- Display decimal values in summary screen [markk 4475]
- Allow entry of KB, MB, or GB values in modify panel [markk 4475]
- Choose and display "best" unit in modify panel [markk 4475]

* Thu Aug  8 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.2-01]
- Remove dangling enable-quota symlinks.  [charlieb 4297]

* Mon Aug  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.1-01]
- Bump quota requirement to version 3.
- Fix fstab template to handle ext3 file systems. [charlieb 4297]
- Remove action script which runs quotacheck - this is now done by rc.sysinit
  during reboot. [charlieb 4297]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-01]
- Changing version to development stream number to 1.5.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Changing version to maintained stream number to 1.4.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.9-01]
- RPM rebuild forced by cvsroot2rpm

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.8-01]
- Move enable-quota back into post-{install,upgrade}. Skip the quotacheck
  if the quota files exist. For an install, they won't. For an upgrade
  from a previously quota'ed system, they will and we don't want to
  bother checking the whole filesystem during the upgrade. For an upgrade
  from a pre-quota system they won't exist, so we need to check.
  Note: /etc/fstab must have the quota options enabled before we attempt
  to run quotacheck or it exits silently [gordonr 3439]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.7-01]
- Turn quotas on (well, off then on) after enabling quotas in case
  we didn't enable them at boot time in an upgrade from version which
  didn't have quotas [gordonr 3439]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.6-01]
- Re-add enable-quotas to post-install, after expansion of /etc/fstab
  [gordonr 3439]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.5-01]
- Updated e-smith-base dependency [gordonr 3439]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.4-01]
- Relocated the scaffolding for /etc/fstab templates to e-smith-base,
  leaving the enable quotas fragment here. The template is also expanded
  with an action in e-smith-base. Updated e-smith-base Requires [gordonr 3439]

* Mon May 13 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.3-01]
- Really fix createlinks [gordonr 3439]

* Mon May 13 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.2-01]
- Actually run enable-quotas in bootstrap-console-save and fix
  createlinks [gordonr 3439]

* Mon May 13 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.1-01]
- Moving to stream 1.3.1 (1.3.0 skipped by accidentally)
- Check all quotas during bootstrap-console-save rather than 
  post-upgrade so that the install completes quickly, even on 
  a machine with lots of disk to check. [gordonr 3439]

* Wed May  8 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.2.8-01]
- Subst scanmail.tmpl -> template name in both quota templates [markk 3029]
- Need to enable quotas before trying to restore them :-) [gordonr 2730]

* Wed May  8 2002 Mark Knox <markk@e-smith.com>
- [1.2.7-01]
- Added gettext in quota warning templates [markk 3029]

* Tue May  7 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.2.6-01]
- Localised "Modify" link on main page [markk 3317]

* Wed May  1 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.2.5-01]
- esmith::AccountDB -> esmith::AccountsDB [schwern 3287]

* Wed Apr 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.2.4-01]
- Rewording SOFT/HARD errors for consistency [gordonr 3027]

* Mon Apr 22 2002 Adrian Chung <adrianc@e-smith.com>
- [1.2.3-01]
- Pass the $user object instead of the $username variable in user-modify-quota.

* Tue Apr 16 2002 Mark Knox <markk@e-smith.com>
- [1.2.2-01]
- Added a missing button in the modify user page [markk 3159]

* Mon Apr 15 2002 Mark Knox <markk@e-smith.com>
- [1.2.1-01]
- Adding warning for Quota::query failure to warnquota & user-modify-quota
  [schwern 2730]
- Testing user-modify-quota [schwern 2729 2730]
- Converted to FormMagick panel and internationalized. Added some POD and
  tests. [markk 3159]
- Added buildtests in %build [markk 3159]

* Thu Mar 7 2002 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-01]
- rollRPM: Rolled version number too 1.2.0-01. Includes patches up to 1.0.0-02.
- DO NOT MAKE ANY FURTHER CHANGES TO THIS FILE, as this is the base version
  being imported into CVS.

* Fri Feb 01 2002 Charlie Brady <charlieb@e-smith.com>
- [1.0.0-02]
- Allow hard and soft quota to be equal. This also allows the quota to be
  removed. See #2729.
- Set quota limits for all users in post-upgrade event. This allows for
  a system restore to have properly set up quotas.

* Tue Dec 11 2001 Jason Miller <jay@e-smith.com>
- [1.0.0-01]
- rollRPM: Rolled version number to 1.0.0-01. Includes patches up to 0.1.1-09.

* Wed Dec  5 2001 Adrian Chung <adrianc@e-smith.com>
- [0.1.1-09]
- Adding new warnquota script that sends mail to users who have exceeded their
  "limit with grace time", and a summary report to admin.
- Adding admin summary template, and user quota warning template to
  /etc/e-smith/templates/usr/lib/e-smith-quota

* Wed Dec  5 2001 Adrian Chung <adrianc@e-smith.com>
- [0.1.1-08]
- Adding check in panel to make sure that soft limit
  is less than hard limit.
- Also insert missing subroutine prototype.

* Thu Nov 15 2001 Adrian Chung <adrianc@e-smith.com>
- [0.1.1-07]
- More text changes to the quota panel.
- Changed kB sizing output to mB sizing.
- Still no genSmallRedCellRightJustified.  Yet.

* Wed Nov 14 2001 Charlie Brady <charlieb@e-smith.com>
- [0.1.1-06]
- Add daily quota warning script. For now, just use a wrapper for
  /usr/sbin/warnquota. In time we will write our own script in perl
  and produce a customised report.

* Wed Nov 14 2001 Adrian Chung <adrianc@e-smith.com>
- [0.1.1-05]
- Update createlinks to create manager quota panel link
- More text changes to quota panel.
- Use genSmallCellRightJustified
- Create "Modify" button.

* Wed Nov 14 2001 Adrian Chung <adrianc@e-smith.com>
- [0.1.1-04]
- Add some wording to panel, and change wording of
  soft and hard limits to "limit with grace time" and
  "immediate limit"
- Still to roll in genSmallCellRight

* Tue Nov 13 2001 Charlie Brady <charlieb@e-smith.com>
- [0.1.1-03]
- Add bare bones web panel which allows setting of soft and hard file limits.

* Mon Nov 12 2001 Charlie Brady <charlieb@e-smith.com>
- [0.1.1-02]
- Add action script to set and modify quotas using properties from the accounts
  db.

* Fri Nov 09 2001 Charlie Brady <charlieb@e-smith.com>
- Initial

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
mkdir -p root/etc/e-smith/events/post-{install,upgrade}
mkdir -p root/etc/e-smith/events/user-{create,modify}
mkdir -p root/etc/e-smith/web/panels/manager/cgi-bin

xgettext -o root/usr/share/locale/en_US/LC_MESSAGES/adminQuotaSummary.po \
    root/etc/e-smith/templates/usr/lib/e-smith-quota/adminQuotaSummary.tmpl
xgettext -o root/usr/share/locale/en_US/LC_MESSAGES/userOverQuota.po \
    root/etc/e-smith/templates/usr/lib/e-smith-quota/userOverQuota.tmpl

perl createlinks
/sbin/e-smith/buildtests 50-e-smith-quota

/sbin/e-smith/generate-lexicons

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --file /etc/rc.d/rc.quota_create 'attr(0755,root,root)' \
    --file /etc/cron.d/warnquota 'attr(0644,root,root)' \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
