class AddShortDescriptionToPost < ActiveRecord::Migration
  def change
    add_column :posts, :short_description, :string
  end
end
