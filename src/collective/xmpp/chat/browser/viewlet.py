from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName
from collective.xmpp.core.interfaces import IXMPPSettings


class ChatData(ViewletBase):
    """ """

    def __init__(self, context, request, view, manager):
        super(ChatData, self).__init__(context, request, view, manager)
        pm = getToolByName(context, 'portal_membership')
        member = pm.getAuthenticatedMember()
        self.username = member.getId()
        info = pm.getMemberInfo(self.username)
        self.fullname = info.get('fullname') or self.username
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IXMPPSettings, check=False)
        self.auto_subscribe = settings.auto_subscribe 
