#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-ruby-beautify
Version  : 0.92.2
Release  : 3
URL      : https://rubygems.org/downloads/ruby-beautify-0.92.2.gem
Source0  : https://rubygems.org/downloads/ruby-beautify-0.92.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-ruby-beautify-bin
BuildRequires : ruby
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support

%description
# RBeautify
This gem provides a cli binary named 'rbeautify' that will pretty up ruby code.

%package bin
Summary: bin components for the rubygem-ruby-beautify package.
Group: Binaries

%description bin
bin components for the rubygem-ruby-beautify package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n ruby-beautify-0.92.2
gem spec %{SOURCE0} -l --ruby > rubygem-ruby-beautify.gemspec

%build
gem build rubygem-ruby-beautify.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
ruby-beautify-0.92.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/ruby-beautify-0.92.2
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/ruby-beautify-0.92.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/README.md
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/RELEASE.md
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/bin/rbeautify
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/lib/beautifier.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/lib/ruby-beautify.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/lib/ruby-beautify/block_end.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/lib/ruby-beautify/block_matcher.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/lib/ruby-beautify/block_start.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/lib/ruby-beautify/config/ruby.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/lib/ruby-beautify/language.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/lib/ruby-beautify/line.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/lib/ruby-beautify/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/ruby-beautify.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/spec/fixtures/ruby.yml
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/spec/rbeautify/block_matcher_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/spec/rbeautify/block_start_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/spec/rbeautify/config/ruby_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/spec/rbeautify/line_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/spec/rbeautify_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ruby-beautify-0.92.2/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/ruby-beautify-0.92.2.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/rbeautify
