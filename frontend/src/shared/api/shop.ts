import { apiClient } from './client'

export type ShopCategory = 'promo_code' | 'subscription' | 'bank_perk'

export interface ShopItem {
  id: string
  category: ShopCategory
  title: string
  description: string
  price: string
  image_url: string | null
  brand_name: string | null
  is_recommended: boolean
}

export interface PurchaseResponse {
  purchase_id: string
  shop_item_id: string
  title: string
  price_paid: string
  payload: string
  purchased_at: string
  new_balance: string
}

export const shopApi = {
  list: (category?: ShopCategory) =>
    apiClient.get<{ items: ShopItem[] }>('/shop/items', {
      params: category ? { category } : undefined,
    }),
  purchase: (shop_item_id: string) =>
    apiClient.post<PurchaseResponse>('/shop/purchase', { shop_item_id }),
}
