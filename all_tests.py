import unittest
from tests import login_manage_test
from tests.manager.companies import add_company_test, edit_company_test, delete_company_test
from tests.customer.rel import login_customer_rel_test
from tests.customer.user_management import add_user_test, duplicate_user_test, edit_user_test, delete_user_test
from tests.manager.contractplan import index_test, add_test, edit_test, delete_test
from tests.customer.rel import companyinfo_test, dashboard_rel_test
from tests.customer.dev.user_management import ui_user_dev_test,add_user_dev_test,search_user_dev_test,sort_column_dev_test,delete_user_dev_test
from tests.customer.dev.groups import ui_groups_test,add_groups_test,sort_groups_test,search_groups_test,edit_groups_test,duplicate_groups_test,delete_groups_test
from tests.customer.dev import dashboard_dev_test
from tests.customer.dev.authority import index_authority_test, add_authority_test, edit_authority_test, duplicate_authority_test, delete_authority_test
from tests.customer.dev.workflow import ui_workflow_test,add_workflow_test,sort_workflow_test,search_workflow_test,edit_workflow_test,delete_workflow_test,duplicate_workflow_test
from tests.customer.dev.table import index_table_test, add_table_test, search_table_test, pagination_table_test, sort_table_test, edit_table_test, duplicate_table_test, delete_table_test
from tests.customer.dev.list_table import index_list_table_test, add_list_table_test, search_list_table_test, sort_list_table_test, pagination_list_table_test, edit_list_table_test, duplicate_list_table_test, delete_list_table_test
from tests.customer.dev.queries import ui_query_test,add_query_test,edit_query_test,duplicate_query_test,sort_query_test,search_query_test,delete_query_test
from tests.customer.dev.incoming_api import ui_incoming_api_test,add_incoming_api_test,change_status_incoming_api_test,delete_incoming_api_test,duplicate_incoming_api_test,edit_incoming_api_test,search_incoming_api_test,sort_incoming_api_test,view_doc_incoming_api_test
from tests.customer.dev.screen import index_screen_test, add_screen_test, search_screen_test, sort_screen_test, pagination_screen_test, edit_screen_test, duplicate_screen_test, delete_screen_test
from tests.customer.dev.outgoing_api import add_outgoing_api_test,delete_outgoing_api_test,duplicate_outgoing_api_test,edit_outgoing_api_test,search_outgoing_api_test,sort_outgoing_api_test,ui_outgoing_api_test
from tests.customer.dev.messages_management import ui_messages_test,add_messages_test,duplicate_messages_test,edit_messages_test,search_messages_test,sort_messages_test,delete_messages_test
from tests.customer.rel.table import index_table_test, pagination_table_test, search_table_test, view_table_test
from tests.customer.rel.outgoing_api_authentication import ui_outgoing_api_auth_test,add_outgoing_api_auth_test,edit_outgoing_api_auth_test,sort_outgoing_api_auth_test,search_outgoing_api_auth_test,delete_outgoing_api_auth_test
from tests.customer.rel.incoming_api_authentication import ui_incoming_api_auth_test,add_incoming_api_auth_test,edit_incoming_api_auth_test,sort_incoming_api_auth_test,search_incoming_api_auth_test,delete_incoming_api_auth_test
from tests.customer.rel.screen_basic_test import screen_basic_test
from tests.customer.dev.screen_basic_test import screen_search_text_test, screen_search_number_test, screen_event_label_test, screen_event_text_test, screen_event_radio_test, screen_event_selection_test, screen_event_attachment_test, screen_event_video_test, screen_event_image_test, screen_event_link_test, screen_event_search_date_test
from tests.screens_sample.screen_loop import loop_condition_test,loop_dynamic_test,loop_checkbox_test
from tests.screens_sample.screen_approval import screen_approval_test, approval_denial_test, approval_re_apply_test, approval_re_approve_test, approval_object_test, approval_applied_user_test,approval_button_superior_test
from tests.screens_sample.screen_event_object import screen_event_button_list_test, screen_event_button_test, screen_event_number_test, screen_event_number_auto_test,screen_event_checkbox_test,screen_event_date_test,screen_event_group_test,screen_event_checkbox_list_test,screen_event_field_value_test
from tests.customer.rel.incoming_api_rel import ui_incoming_api_rel_test, search_incoming_api_rel_test, sort_incoming_api_rel_test, view_doc_incoming_api_rel_test


def all_suites():
    all_testcases = [
        # Login management
        login_manage_test.suite(),

        # Company management
        add_company_test.suite(), 
        edit_company_test.suite(),
        delete_company_test.suite(),

        # contract plan manager
        index_test.suite(),
        add_test.suite(),
        edit_test.suite(),
        delete_test.suite(),

        # Login REL
        login_customer_rel_test.suite(),

        # Dashboard rel
        dashboard_rel_test.suite(),

        # Dashboard dev
        dashboard_dev_test.suite(),

        # Company info
        companyinfo_test.suite(),

        # User management in REL
        add_user_test.suite(), 
        duplicate_user_test.suite(),
        edit_user_test.suite(),
        delete_user_test.suite(),
        
        # User management in DEV
        ui_user_dev_test.suite(),
        add_user_dev_test.suite(),
        search_user_dev_test.suite(),
        sort_column_dev_test.suite(),
        delete_user_dev_test.suite(),

        # Authority management in DEV
        index_authority_test.suite(),
        add_authority_test.suite(),
        edit_authority_test.suite(),
        duplicate_authority_test.suite(),
        delete_authority_test.suite(),
        
        # Groups management in DEV
        ui_groups_test.suite(),
        add_groups_test.suite(),
        sort_groups_test.suite(),
        search_groups_test.suite(),
        edit_groups_test.suite(),
        duplicate_groups_test.suite(),
        delete_groups_test.suite(),

        # Workflow management in DEV
        ui_workflow_test.suite(),
        add_workflow_test.suite(),
        edit_workflow_test.suite(),
        duplicate_workflow_test.suite(),
        sort_workflow_test.suite(),
        search_workflow_test.suite(),
        delete_workflow_test.suite(),

        # Table management in dev
        index_table_test.suite(),
        add_table_test.suite(),
        search_table_test.suite(),
        pagination_table_test.suite(),
        sort_table_test.suite(),
        edit_table_test.suite(),
        duplicate_table_test.suite(),
        delete_table_test.suite(),

        # List Table management in dev
        index_list_table_test.suite(),
        add_list_table_test.suite(),
        search_list_table_test.suite(),
        sort_list_table_test.suite(),
        pagination_list_table_test.suite(),
        edit_list_table_test.suite(),
        duplicate_list_table_test.suite(),
        delete_list_table_test.suite(),
        
        # # Query settings in DEV
        # ui_query_test.suite(),
        # add_query_test.suite(),
        # duplicate_query_test.suite(),
        # edit_query_test.suite(),  
        # sort_query_test.suite(),
        # search_query_test.suite(),
        # delete_query_test.suite(),

        # Messages management in DEV
        ui_messages_test.suite(),
        add_messages_test.suite(),
        duplicate_messages_test.suite(),
        edit_messages_test.suite(),
        search_messages_test.suite(),
        sort_messages_test.suite(),
        delete_messages_test.suite(),

        # Incoming API Authorizations in REL
        ui_incoming_api_auth_test.suite(),
        add_incoming_api_auth_test.suite(),
        edit_incoming_api_auth_test.suite(),
        search_incoming_api_auth_test.suite(),
        sort_incoming_api_auth_test.suite(),
        delete_incoming_api_auth_test.suite(),

        # Incoming API in DEV
        ui_incoming_api_test.suite(),
        add_incoming_api_test.suite(),
        view_doc_incoming_api_test.suite(),
        change_status_incoming_api_test.suite(),
        duplicate_incoming_api_test.suite(),
        edit_incoming_api_test.suite(),
        search_incoming_api_test.suite(),
        sort_incoming_api_test.suite(),
        delete_incoming_api_test.suite(),

        # Incoming API in REL
        ui_incoming_api_rel_test.suite(),
        search_incoming_api_rel_test.suite(),
        sort_incoming_api_rel_test.suite(),
        view_doc_incoming_api_rel_test.suite(),

        # Screen management in dev
        index_screen_test.suite(),
        add_screen_test.suite(),
        search_screen_test.suite(),
        sort_screen_test.suite(),
        pagination_screen_test.suite(),
        edit_screen_test.suite(),
        duplicate_screen_test.suite(),
        delete_screen_test.suite(),

        # Outgoing API Authentications in REL
        ui_outgoing_api_auth_test.suite(),
        add_outgoing_api_auth_test.suite(),
        edit_outgoing_api_auth_test.suite(),
        search_outgoing_api_auth_test.suite(),
        sort_outgoing_api_auth_test.suite(),
        delete_outgoing_api_auth_test.suite(),
        
        # Outgoing API in DEV
        ui_outgoing_api_test.suite(),
        add_outgoing_api_test.suite(),
        duplicate_outgoing_api_test.suite(),
        edit_outgoing_api_test.suite(),
        search_outgoing_api_test.suite(),
        sort_outgoing_api_test.suite(),
        delete_outgoing_api_test.suite(),

        # Table management in rel
        index_table_test.suite(),
        pagination_table_test.suite(),
        search_table_test.suite(),
        view_table_test.suite(),

        # Test screen rel example
        screen_basic_test.suite(),

        # Screen Loop Event
        loop_condition_test.suite(),
        loop_dynamic_test.suite(),
        loop_checkbox_test.suite(),

        # Test screen search dev example
        screen_search_text_test.suite(),
        screen_search_number_test.suite(),
        screen_event_label_test.suite(),
        screen_event_text_test.suite(),
        screen_event_radio_test.suite(),
        screen_event_selection_test.suite(),
        screen_event_attachment_test.suite(),
        screen_event_image_test.suite(),
        screen_event_video_test.suite(),
        screen_event_link_test.suite(),
        screen_event_search_date_test.suite(),

        # Test Approval screen
        screen_approval_test.suite(),
        approval_object_test.suite(),
        approval_denial_test.suite(), 
        approval_re_apply_test.suite(),
        approval_re_approve_test.suite(),
        approval_applied_user_test.suite(),
        approval_button_superior_test.suite(),

        # Screen Event Object
        screen_event_number_test.suite(),
        screen_event_number_auto_test.suite(),
        screen_event_checkbox_test.suite(),
        screen_event_date_test.suite(),
        screen_event_group_test.suite(),
        screen_event_checkbox_list_test.suite(),
        screen_event_field_value_test.suite(),
        screen_event_button_test.suite(),
        screen_event_button_list_test.suite(),
    ]

    return unittest.TestSuite(all_testcases)

runner = unittest.TextTestRunner(failfast=False)
runner.run(all_suites())

if __name__ == '__main__':
    unittest.main()