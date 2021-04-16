
import nose
import os

import ckanext.dcatapit.helpers as helpers

eq_ = nose.tools.eq_
ok_ = nose.tools.ok_

def test_get_dcatapit_package_schema():
    schema = helpers.get_dcatapit_package_schema()
    ok_(schema)
    eq_(schema[0].get('name'), 'identifier')

def test_get_dcatapit_organization_schema():
    schema = helpers.get_dcatapit_organization_schema()
    ok_(schema)
    eq_(schema[0].get('name'), 'email')

def test_get_dcatapit_configuration_schema():
    schema = helpers.get_dcatapit_configuration_schema()
    ok_(schema)
    eq_(schema[0].get('name'), 'ckanext.dcatapit_configpublisher_name')

def test_get_dcatapit_resource_schema():
    schema = helpers.get_dcatapit_resource_schema()
    ok_(schema)
    eq_(schema[0].get('name'), 'distribution_format')

def test_get_vocabulary_items():
    # Load themes voc    
    from ckanext.dcatapit.commands.dcatapit import EUROPEAN_THEME_NAME, do_load

    path = os.path.join(os.path.dirname(__file__),
                    '..', '..', '..', 'vocabularies', 'data-theme-skos.rdf')
    do_load(EUROPEAN_THEME_NAME, filename=path)    
    
    # test it
    vocabularies_items = helpers.get_vocabulary_items(EUROPEAN_THEME_NAME)
    ok_(vocabularies_items)
    
def test_list_to_string():
    test_list = ['test1', 'test2', 'test3']
    test_string = helpers.list_to_string(test_list)
    ok_(isinstance(test_string, str))

def test_format():
    value = helpers.format('14-11-2011', '%Y-%m-%d', 'date')
    eq_(value, '2011-11-14')
    # invalid value, but valid format
    value = helpers.format('14-11-0011', '%Y-%m-%d', 'date')
    eq_(value, '14-11-0011')


def test_org_context():
    # ensure ctx are separated, and no data is leaked between them
    ctx1 = helpers.get_org_context()
    ctx1['test'] = True
    ctx2 = helpers.get_org_context()
    
    assert ctx2.get('test') is None
