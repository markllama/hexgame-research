class CreateMaps < ActiveRecord::Migration
  def self.up
    create_table :maps do |t|
      t.string :name
      t.string :game
      t.integer :size_hx
      t.integer :size_hy
      t.integer :origin_hx
      t.integer :origin_hy

      t.timestamps
    end
  end

  def self.down
    drop_table :maps
  end
end
