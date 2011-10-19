from django.db import models

class LivePostManager(models.Manager):
  """
  Custom manager for the Entry model, providing shortcuts for
  filtering by entry status.
  
  """

#  def get_query_set(self):
    #pdb.set_trace()
    #return super(LivePostManager, self).get_query_set().filter(status__exact=self.model.LIVE_STATUS)

#  def get_live_posts(self):
  def get_query_set(self):
    """
    Overrides the default ``QuerySet`` to only include Entries
    with a status of 'live'.
    
    """
    return super(LivePostManager, self).get_query_set().filter(status__exact=self.model.LIVE_STATUS)
