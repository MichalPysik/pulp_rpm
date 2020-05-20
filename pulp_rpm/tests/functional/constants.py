# coding=utf-8
"""Constants for Pulp RPM plugin tests."""
from urllib.parse import urljoin

from pulp_smash import config
from pulp_smash.pulp3.constants import (
    BASE_CONTENT_PATH,
    BASE_DISTRIBUTION_PATH,
    BASE_REPO_PATH,
    BASE_PATH,
    BASE_PUBLICATION_PATH,
    BASE_REMOTE_PATH,
)

RPM_COPY_PATH = urljoin(BASE_PATH, 'rpm/copy/')
"""The URL used for copying RPM content between repos."""

PULP_FIXTURES_BASE_URL = config.get_config().get_fixtures_url()

DOWNLOAD_POLICIES = ["immediate", "on_demand", "streamed"]

DRPM_UNSIGNED_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, 'drpm-unsigned/')
"""The URL to a repository with unsigned DRPM packages."""

RPM_PACKAGE_CONTENT_NAME = 'rpm.package'

RPM_PACKAGECATEGORY_CONTENT_NAME = 'rpm.packagecategory'

RPM_PACKAGEGROUP_CONTENT_NAME = 'rpm.packagegroup'

RPM_PACKAGELANGPACKS_CONTENT_NAME = 'rpm.packagelangpacks'

RPM_ADVISORY_CONTENT_NAME = 'rpm.advisory'

RPM_ALT_LAYOUT_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, 'rpm-alt-layout/')
"""The URL to a signed RPM repository. See :data:`RPM_SIGNED_FIXTURE_URL`."""

RPM_CONTENT_PATH = urljoin(BASE_CONTENT_PATH, 'rpm/packages/')
"""The location of RPM packages on the content endpoint."""

RPM_NAMESPACES = {
    'metadata/common': 'http://linux.duke.edu/metadata/common',
    'metadata/filelists': 'http://linux.duke.edu/metadata/filelists',
    'metadata/other': 'http://linux.duke.edu/metadata/other',
    'metadata/repo': 'http://linux.duke.edu/metadata/repo',
    'metadata/rpm': 'http://linux.duke.edu/metadata/rpm',
}
"""Namespaces used by XML-based RPM metadata.

Many of the XML files generated by the ``createrepo`` utility make use of these
namespaces. Some of the files that use these namespaces are listed below:

metadata/common
    Used by ``repodata/primary.xml``.

metadata/filelists
    Used by ``repodata/filelists.xml``.

metadata/other
    Used by ``repodata/other.xml``.

metadata/repo
    Used by ``repodata/repomd.xml``.

metadata/rpm
    Used by ``repodata/repomd.xml``.
"""

RPM_DISTRIBUTION_PATH = urljoin(BASE_DISTRIBUTION_PATH, 'rpm/rpm/')

RPM_REMOTE_PATH = urljoin(BASE_REMOTE_PATH, 'rpm/rpm/')

RPM_REPO_PATH = urljoin(BASE_REPO_PATH, 'rpm/rpm/')

RPM_PUBLICATION_PATH = urljoin(BASE_PUBLICATION_PATH, 'rpm/rpm/')

RPM_SHA512_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, 'rpm-with-sha-512/')
"""The URL to an RPM repository with sha512 checksum."""

RPM_SIGNED_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, 'rpm-signed/')
"""The URL to a repository with signed RPM packages."""

RPM_SINGLE_REQUEST_UPLOAD = urljoin(BASE_PATH, 'content/rpm/packages/')

RPM_UNSIGNED_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, 'rpm-unsigned/')
"""The URL to a repository with unsigned RPM packages."""

RPM_INVALID_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, 'rpm-missing-filelists/')

RPM_PACKAGE_COUNT = 35
"""The number of packages available at
:data:`RPM_SIGNED_FIXTURE_URL` and :data:`RPM_UNSIGNED_FIXTURE_URL`
"""

RPM_PACKAGECATEGORY_COUNT = 1
"""The number of packagecategories."""

RPM_PACKAGEGROUP_COUNT = 2
"""The number of packagegroups."""

RPM_PACKAGELANGPACKS_COUNT = 1
"""The number of packagelangpacks."""

RPM_ADVISORY_COUNT = 4
"""The number of updated record units."""

RPM_FIXTURE_SUMMARY = {
    RPM_PACKAGE_CONTENT_NAME: RPM_PACKAGE_COUNT,
    RPM_ADVISORY_CONTENT_NAME: RPM_ADVISORY_COUNT,
    RPM_PACKAGECATEGORY_CONTENT_NAME: RPM_PACKAGECATEGORY_COUNT,
    RPM_PACKAGEGROUP_CONTENT_NAME: RPM_PACKAGEGROUP_COUNT,
    RPM_PACKAGELANGPACKS_CONTENT_NAME: RPM_PACKAGELANGPACKS_COUNT,
}
"""The breakdown of how many of each type of content unit are present in the
standard repositories, i.e. :data:`RPM_SIGNED_FIXTURE_URL` and
:data:`RPM_UNSIGNED_FIXTURE_URL`.  This matches the format output by the
"content_summary" field on "../repositories/../versions/../".
"""

RPM_EPEL_URL = 'https://dl.fedoraproject.org/pub/epel/7Server/x86_64/'
"""The URL to large repository. EPEL7.

.. NOTE:: This repository is not generated by pulp-fixtures.
"""

RPM_LONG_UPDATEINFO_FIXTURE_URL = urljoin(
    PULP_FIXTURES_BASE_URL, 'rpm-long-updateinfo/'
)
"""The URL to RPM with a long updateinfo.xml."""

RPM_MODULAR_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, 'rpm-with-modules/')
"""The URL to a modular RPM repository."""

RPM_MODULES_COUNT = 10
"""The number of modules present on `RPM_MODULAR_FIXTURE_URL`."""

RPM_MODULES_DEFAULTS_COUNT = 3
"""The number of modules-default present on `RPM_MODULAR_FIXTURE_URL`."""

RPM_MODULES_CONTENT_NAME = 'rpm.modulemd'

RPM_MODULES_DEFAULTS_CONTENT_NAME = 'rpm.modulemd_defaults'

RPM_ADVISORY_MODULAR_COUNT = 6

RPM_MODULAR_FIXTURE_SUMMARY = {
    RPM_PACKAGE_CONTENT_NAME: RPM_PACKAGE_COUNT,
    RPM_ADVISORY_CONTENT_NAME: RPM_ADVISORY_MODULAR_COUNT,
    RPM_MODULES_CONTENT_NAME: RPM_MODULES_COUNT,
    RPM_MODULES_DEFAULTS_CONTENT_NAME: RPM_MODULES_DEFAULTS_COUNT,
    RPM_PACKAGECATEGORY_CONTENT_NAME: RPM_PACKAGECATEGORY_COUNT,
    RPM_PACKAGEGROUP_CONTENT_NAME: RPM_PACKAGEGROUP_COUNT,
    RPM_PACKAGELANGPACKS_CONTENT_NAME: RPM_PACKAGELANGPACKS_COUNT,
}
"""The breakdown of how many of each type of content unit are present in the
i.e. :data:`RPM_MODULAR_FIXTURE_URL`."""

RPM_PACKAGE_DATA = {
    'name': 'kangaroo',
    'epoch': '0',
    'version': '0.3',
    'release': '1',
    'arch': 'noarch',
    'description': 'A modular RPM fixture for testing Pulp.',
    'summary': 'hop like a kangaroo in Australia',
    'rpm_license': 'Public Domain',
    'rpm_group': 'Unspecified',
    'rpm_vendor': '',
    # TODO: Complete this information once we figure out how to serialize
    # everything nicely
}
"""The metadata for one RPM package."""

RPM_PACKAGE_DATA2 = {
    'name': 'duck',
    'epoch': '0',
    'version': '0.7',
    'release': '1',
    'arch': 'noarch',
    'description': 'A dummy package of duck',
    'summary': 'A dummy package of duck',
    'rpm_license': 'GPLv2',
    'rpm_group': 'Internet/Applications',
    'rpm_vendor': '',
    # TODO: Complete this information once we figure out how to serialize
    # everything nicely
}
"""The metadata for one RPM package."""

RPM_PACKAGE_NAME = '{}'.format(RPM_PACKAGE_DATA['name'])
"""The name of one RPM package."""

RPM_PACKAGE_FILENAME = '{}-{}-{}.{}.rpm'.format(
    RPM_PACKAGE_DATA['name'],
    RPM_PACKAGE_DATA['version'],
    RPM_PACKAGE_DATA['release'],
    RPM_PACKAGE_DATA['arch'],
)
"""The filename of one RPM package."""

RPM_PACKAGE_FILENAME2 = '{}-{}-{}.{}.rpm'.format(
    RPM_PACKAGE_DATA2['name'],
    RPM_PACKAGE_DATA2['version'],
    RPM_PACKAGE_DATA2['release'],
    RPM_PACKAGE_DATA2['arch'],
)
"""The filename of one RPM package."""

RPM_REFERENCES_UPDATEINFO_URL = urljoin(
    PULP_FIXTURES_BASE_URL, 'rpm-references-updateinfo/'
)
"""The URL to a repository with ``updateinfo.xml`` containing references.

This repository includes advisory with reference element (0, 1 or 2 references)
and without it.
"""

RPM_RICH_WEAK_FIXTURE_URL = urljoin(
    PULP_FIXTURES_BASE_URL, 'rpm-richnweak-deps/'
)
"""The URL to an RPM repository with weak and rich dependencies."""

RPM_SIGNED_URL = urljoin(RPM_SIGNED_FIXTURE_URL, RPM_PACKAGE_FILENAME)
"""The path to a single signed RPM package."""

RPM_SIGNED_URL2 = urljoin(RPM_SIGNED_FIXTURE_URL, RPM_PACKAGE_FILENAME2)
"""The path to a single signed RPM package."""

RPM_UNSIGNED_URL = urljoin(RPM_UNSIGNED_FIXTURE_URL, RPM_PACKAGE_FILENAME)
"""The path to a single unsigned RPM package."""

RPM_UPDATED_UPDATEINFO_FIXTURE_URL = urljoin(
    PULP_FIXTURES_BASE_URL, 'rpm-updated-updateinfo/'
)
"""The URL to a repository containing UpdateRecords (Advisory) with the same IDs
as the ones in the standard repositories, but with different metadata.

Note: This repository uses unsigned RPMs.
"""

RPM_ADVISORY_UPDATED_VERSION_URL = urljoin(
    PULP_FIXTURES_BASE_URL, 'rpm-updated-updateversion'
)
"""The URL to a repository containing Advisories with same ID as the ones in the standard
unsigned rpm repository, but with updated Advisory version.
"""

RPM_ADVISORY_DIFFERENT_PKGLIST_URL = urljoin(
    PULP_FIXTURES_BASE_URL, 'rpm-advisory-diffpkgs'
)
"""The URL to a repository containing Advisories with same ID and version as the ones in the
standard unsigned rpm repository, but with different pkglist.
"""

RPM_ADVISORY_DIFFERENT_REPO_URL = urljoin(
    PULP_FIXTURES_BASE_URL, 'rpm-advisory-diff-repo'
)
"""The URL to a repository containing Advisories with same ID and version as the ones in the
standard unsigned rpm repository, but with different update_date and packages intersection.
"""

RPM_ADVISORY_INCOMPLETE_PKG_LIST_URL = urljoin(
    PULP_FIXTURES_BASE_URL, 'rpm-advisory-incomplete-package-list'
)
"""The URL to a repository containing Advisories with same update_date and version as the ones
in the standard unsigned rpm repository, but pkglist intersection is non-empty and not equal
to either pkglist.
"""

RPM_ADVISORY_NO_DATES = urljoin(
    PULP_FIXTURES_BASE_URL, 'rpm-advisory-no-dates'
)
"""The URL to a repository containing Advisories with same id and version as the ones
in the standard unsigned rpm repository, but no update_date or issue_date.
"""

RPM_ADVISORY_TEST_ID = 'RHEA-2012:0056'
RPM_ADVISORY_TEST_ID_NEW = 'RHEA-2012:0058'
"""The ID of an UpdateRecord (advisory/erratum).

The package contained on this advisory is defined by
:data:`RPM_UPDATERECORD_RPM_NAME` and the advisory is present in the standard
repositories, i.e. :data:`RPM_SIGNED_FIXTURE_URL` and
:data:`RPM_UNSIGNED_FIXTURE_URL`.
"""
RPM_ADVISORY_TEST_REMOVE_COUNT = 3
RPM_ADVISORY_TEST_ADDED_COUNT = 6


RPM_UPDATERECORD_RPM_NAME = 'gorilla'
"""The name of the RPM named by :data:`RPM_UPDATERECORD_ID`."""

RPM_WITH_NON_ASCII_NAME = 'rpm-with-non-ascii'

RPM_WITH_NON_ASCII_URL = urljoin(
    PULP_FIXTURES_BASE_URL,
    'rpm-with-non-ascii/{}-1-1.fc25.noarch.rpm'.format(
        RPM_WITH_NON_ASCII_NAME
    ),
)
"""The URL to an RPM with non-ascii metadata in its header."""

RPM_WITH_NON_UTF_8_NAME = 'rpm-with-non-utf-8'

RPM_WITH_NON_UTF_8_URL = urljoin(
    PULP_FIXTURES_BASE_URL,
    'rpm-with-non-utf-8/{}-1-1.fc25.noarch.rpm'.format(
        RPM_WITH_NON_UTF_8_NAME
    ),
)
"""The URL to an RPM with non-UTF-8 metadata in its header."""

SRPM_UNSIGNED_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, 'srpm-unsigned/')
"""The URL to a repository with unsigned SRPM packages."""

SRPM_UNSIGNED_FIXTURE_ADVISORY_COUNT = 2
"""Count of advisories in the repository."""

SRPM_UNSIGNED_FIXTURE_PACKAGE_COUNT = 3
"""Count of packages in the repository."""

UPDATERECORD_CONTENT_PATH = urljoin(BASE_CONTENT_PATH, 'rpm/advisories/')
"""The location of RPM UpdateRecords on the content endpoint."""

KICKSTART_CONTENT_PATH = urljoin(BASE_CONTENT_PATH, 'rpm/distribution_trees/')
"""The location of RPM Distribution Trees on the content endpoint."""

RPM_KICKSTART_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, 'rpm-kickstart/')

RPM_KICKSTART_CONTENT_NAME = 'rpm.distribution_tree'

RPM_KICKSTART_COUNT = 1

RPM_KICKSTART_FIXTURE_SUMMARY = {
    RPM_KICKSTART_CONTENT_NAME: RPM_KICKSTART_COUNT
}

PULP_FIXTURES_COMMON_URL = 'https://github.com/pulp/pulp-fixtures/raw/master/common/'
PRIVATE_GPG_KEY_URL = urljoin(PULP_FIXTURES_COMMON_URL, 'GPG-PRIVATE-KEY-pulp-qe')


CENTOS6_URL = "http://mirror.centos.org/centos-6/6.10/os/x86_64/"
CENTOS7_URL = "http://mirror.linux.duke.edu/pub/centos/7/os/x86_64/"
CENTOS8_KICKSTART_APP_URL = "http://mirror.linux.duke.edu/pub/centos/8/AppStream/x86_64/kickstart/"
CENTOS8_KICKSTART_BASEOS_URL = "http://mirror.linux.duke.edu/pub/centos/8/BaseOS/x86_64/kickstart/"
CENTOS8_APPSTREAM_URL = "http://mirror.linux.duke.edu/pub/centos/8/AppStream/x86_64/os/"
CENTOS8_BASEOS_URL = "http://mirror.linux.duke.edu/pub/centos/8/BaseOS/x86_64/os/"
EPEL7_URL = "https://dl.fedoraproject.org/pub/epel/7/x86_64/"

PULP_TYPE_ADVISORY = 'rpm.advisory'
PULP_TYPE_PACKAGE = 'rpm.package'
